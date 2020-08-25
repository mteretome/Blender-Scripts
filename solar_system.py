
import bpy
import random
import math
import bmesh

'''
colors
'''
yellow = (1, 1, 0,1.0)              #sun
red = (0.8, 0, 0,1.0)               #mars
dark_blue = (0,0,0.6,1.0)           #neptune
turquoise = (0,0.6,0.6,1.0)         #uranus
dark_orange = (0.8, 0.4, 0,1.0)     #mercury
light_brown = (0.7, 0.4, 0.2,1.0)   #venus 
dark_turquoise = (0,0.4,0.4,1.0)    #earth
light_orange  = (1, 0.6, 0.2,1.0)   #saturn  
pink = (0.8, 0.5, 0.5,1.0)          #jupiter 
white = (1,1,1,1.0)                 #orbits


'''
makes spheres
n is the name of the sphere and d is the diameter
'''
def make_sphere(n, d):
    if(isinstance(n,str)):
        
        mesh_name = n + "_mesh"
        ob_name = n + "_ob"
        #create empty mesh and obj
        mesh_name = bpy.data.meshes.new(n)
        ob_name = bpy.data.objects.new(n, mesh_name)
        #add obj to scene
        bpy.context.collection.objects.link(ob_name)
        bpy.context.view_layer.objects.active = ob_name
        ob_name.select_set(state=True)
        
        #construct bmesh sphere and assign it to mesh
        bm = bmesh.new()
        bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=d)
        bm.to_mesh(mesh_name)
        bm.free()
        return ob_name
    else:
        print("Error: n must be a string")
        return None

'''
color ANY object
'''
def color(ob, color):
  #create color material
  material = bpy.data.materials.new('material')
  #add to the obj
  ob.data.materials.append(material)
  #color it accordingly
  ob.data.materials[0].diffuse_color  = color



    
'''
create each planet object and adds them to a planet list
'''
def create_planets():
    planets = []
    '''
    make each planet
    '''
    planets.append(make_sphere("Mercury", 0.1))
    planets.append(make_sphere("Venus", 0.4))
    planets.append(make_sphere("Earth", 0.4))
    planets.append(make_sphere("Mars", 0.2))
    planets.append(make_sphere("Jupiter" , 5.1))
    planets.append(make_sphere("Saturn", 4.1))
    planets.append(make_sphere("Neptune", 1.6))
    planets.append(make_sphere("Uranus", 1.))
    #no pluto, sorry

    '''
    assign location
    '''
    planets[0].location = (52.1,0,0)
    planets[1].location = (53.9,0,0)
    planets[2].location = (55.4,0,0)
    planets[3].location = (58.2,0,0)
    planets[4].location = (78,0,0)
    planets[5].location = (101.3,0,0)
    planets[6].location = (211.6,0,0)
    planets[7].location = (262.4,0,0)

    '''
    color
    '''
    color(planets[0], dark_orange)
    color(planets[1], light_brown)
    color(planets[2], dark_turquoise)
    color(planets[3], red)
    color(planets[4], pink)
    color(planets[5], light_orange)
    color(planets[6], dark_blue)
    color(planets[7], turquoise)

    return planets

'''
should smooth ANY object
'''      
def smooth(ob):
    bpy.ops.object.shade_smooth()
    bpy.ops.object.shade_smooth()
    bpy.ops.object.modifier_add(type='SUBSURF')
    
'''
function to generate solar system
'''
def make_system():
    planets = create_planets()
    for ob in planets:
        smooth(ob)
    
    #make sun
    sun = make_sphere("Sun", 40)
    sun.location = (0,0,0)
    color(sun, yellow)
    smooth(sun)
    
    return planets

    
#create orbit paths of planets
def orbit_paths(ob):
    orbit_name = "orbit_" + ob.name
    r = ob.location[0]
    bpy.ops.curve.primitive_bezier_circle_add(radius=r,
                                              enter_editmode=False,
                                              location=(0.0, 0.0, 0.0),
                                              rotation=(0.0, 0.0, 0.0))
    bpy.context.active_object.name = orbit_name
    return orbit_name    

#function to make planets rotate the sun
def orbit(planets):
    #attach each planet to its orbit 
    
    for ob in planets:
      orbit_paths(ob)
      name = ob.name
      orb_name = "orbit_" + ob.name
      ob.location = (0,0,0)
      #bounds each planet to its orbit
      const = bpy.data.objects[name].constraints.new('FOLLOW_PATH')
      ob.constraints[0].target = bpy.data.objects[orb_name]
      bpy.data.objects[orb_name].select_set(state=False)
      
      
      '''
      #this section is supposed to make the animation but I kept getting an error I couldnt fix
      override={'constraint':bpy.data.objects[name].constraints["Follow Path"]}
      bpy.ops.constraint.followpath_path_animate(override,constraint=const.name)
      bpy.ops.screen.animation_play()
      '''        
      
     
  
'''
function to delete ALL objects       
'''
def del_all():
    bpy.ops.object.select_all(action='SELECT')
    for ob in bpy.context.selectable_objects:
        bpy.ops.object.delete(use_global=False)
        
    
        
del_all()  
planets = make_system()
orbit(planets)



import bpy
import random
import math


#generate n balls in random locations & returns list with balls
def create_balls(n):
    balls = []
    #makes the objects
    for i in range(n): 
        x, y, z  = random.randint(-10,10), random.randint(-10,10), 0  
        bpy.ops.mesh.primitive_uv_sphere_add( 
        location = [ x, y, z] )
        ob = bpy.ops.object
        balls.append(ob)
        #smoothes the spheres 
        bpy.ops.object.shade_smooth()
        bpy.ops.object.shade_smooth()
        bpy.ops.object.modifier_add(type='SUBSURF')
    return balls
      
        

#function to delete ALL objects       
def del_all():
    bpy.ops.object.select_all(action='SELECT')
    for ob in bpy.context.selectable_objects:
        bpy.ops.object.delete(use_global=False)
        
        
#bounce         
def bounce(lst):
    bpy.ops.object.select_all(action='SELECT')
    start_pos = []
    objs = []
    num_obs = 0
    
    for ob in bpy.context.selectable_objects:
        start_pos.append(ob.location)
        objs.append(ob)
        num_obs+=1
     
 
    frame_num = 0 
    #for ob in bpy.context.selectable_objects:
    count_objs = 0
    for ob in objs:
        
        positions=[]
        positions.append(start_pos[count_objs])
        x, y = ob.location[0], ob.location[1]
        for i in range(20):
            z = math.sin(i)*10+10 #using sin to replicated bouncing
            positions.append((x,y,z))
            print(*positions, sep = " ")
        positions.append(start_pos[count_objs])
        #asssigns positiosp and creates bouncing
        for position in positions:
            bpy.context.scene.frame_set(frame_num)
            ob.location = position
            ob.keyframe_insert(data_path="location", index = -1)
            frame_num +=10

        #reset the frame    
        count_objs+=1
        frame_num=0;
        
   
    
del_all()
balls = create_balls(10)       
bounce(balls)
 
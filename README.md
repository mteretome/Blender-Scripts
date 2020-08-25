# Blender Bouncing Balls
 a blender script  that creates n spheres and makes them into n balls and then animates them so it appears they bounce

    - automated tasks: creating smooth spheres, bouncing effect
    - graphics: n balls created that bounce on command

## To run this file on blender:
	- Install blender from https://www.blender.org/download/
### Way #1 
    1. Open a new Blender file
    2. Change the editor type to text editor
    3. From the text tab in the text editor, you can either copy and paste the code to the text editor or directly open the code from the test editor
    4. Press ALT+P to run the script (from a windows) or do it directly by opening the text tab and pressing Run Script
### Way #2
    1. Open a new Blender file
    2. Change editor type to text editor
    3. Copy and paste the following text with the correct path to the script you wish to run:
        filename = "/full/path/to/bouncing_balls.py"
        exec(compile(open(filename).read(), filename, 'exec'))
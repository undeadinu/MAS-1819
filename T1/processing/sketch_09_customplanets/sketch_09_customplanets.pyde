add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import *
from io import *

def setup():
    size(800,450,P3D)
    cam = PeasyCam(this,500)
    noStroke()
    
    global bgimage
    bgimage = loadImage("galactic_starfield_800x450.jpg")

    global planet1, planet2, planet3, planet4
    rp = RulePyramid()
    rt = RuleTapered()
    
    b = Box(0,0,0,100,100,100)
    planet1 = b.get_mesh()
    
    for i in range(2):
        planet1 = rt.replace(planet1, 0.5, 20, True)
    planet1 = rp.replace(planet1, 8)
    planet1 = rt.replace(planet1, 0.05, 0, True)
    
    export_obj(planet1,"obj_exports/sun.obj")
        
    b = Dodecahedron(0,0,0,40)
    planet2 = b.get_mesh()
    for i in range(3):
        planet2 = rp.replace(planet2, 10-i*6)
        
    b = Box(0,0,0,30,30,30)
    planet3 = b.get_mesh()
    for i in range(3):
        planet3 = rp.replace(planet3, 10-i*6)
        
    b = Box(0,0,0,20,20,20)
    planet4 = b.get_mesh()
    for i in range(2):
        planet4 = rp.replace(planet4, 10-i*6)
        
def draw():
    background(bgimage)
    #image(bgimage,0,0,width,height)
    rotateX(PI/3)
    # rotateZ(frameCount/100.0)
    # directionalLight(255,  0,127,   0, 0, -1)
    # directionalLight(  0,127,255,  -1, 0, 0.3)
    # directionalLight(127,255,  0, 0.5, 1, 0.3)
    # directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    # point lights
    pushMatrix()
    # to p2
    rotateZ(frameCount/100.0)
    translate(200,0,0)
    # blue light
    pointLight(0,127,255,0,0,0)
    # to its moon
    rotateZ(-frameCount/50.0)
    translate(100,0,0)
    # pink light
    pointLight(255,0,127,0,0,0)
    popMatrix()
    
    pushMatrix()
    # to p3
    rotateZ(-frameCount/60.0)
    translate(350,0,0)
    # green light
    pointLight(0,255,127,0,0,0)
    popMatrix()
    
    
    # display the sun (p1)
    pushMatrix()
    rotateZ(-frameCount/200.0)
    for f in planet1.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
    popMatrix()
      
    # display p2 with its moon
    pushMatrix()
    # rotation around the sun
    rotateZ(frameCount/100.0)
    # distance from the sun
    translate(200,0,0)
    pushMatrix()
    # rotation around it's own axis
    rotateZ(frameCount/100.0)
    for f in planet2.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
    popMatrix()
    
    # moon (p4)
    pushMatrix()
    rotateZ(-frameCount/50.0)
    translate(100,0,0)
    rotateZ(-frameCount/40.0)
    for f in planet4.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
    popMatrix()
    # pop matrix of p2
    popMatrix()
    
    # display p3
    pushMatrix()
    rotateZ(-frameCount/60.0)
    translate(350,0,0)
    rotateZ(-frameCount/60.0)
    for f in planet3.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
    popMatrix()
    
    # export every frame into an image
    if frameCount%5==0 and frameCount<-1:
        saveFrame("export/####.png")
    

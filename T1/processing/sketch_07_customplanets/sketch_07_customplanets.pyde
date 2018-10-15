add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import *

def setup():
    size(800,450,P3D)
    cam = PeasyCam(this,500)
    noStroke()

    global planet1, planet2, planet3, planet4
    rp = RulePyramid()

    b = Box(0,0,0,100,100,100)
    planet1 = b.get_mesh()
    for i in range(4):
        planet1 = rp.replace(planet1, 10-i*6)
        
    b = Box(0,0,0,60,60,60)
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
    background(20)
    rotateX(PI/3)
    # rotateZ(frameCount/100.0)
    directionalLight(255,  0,127,   0, 0, -1)
    directionalLight(  0,127,255,  -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    # display the sun (p1)
    pushMatrix()
    rotateZ(frameCount/200.0)
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
    # rotation around it's own axis
    rotateZ(frameCount/100.0)
    for f in planet2.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
    
    # moon (p4)
    pushMatrix()
    rotateZ(-frameCount/50.0)
    translate(100,0,0)
    for f in planet4.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
    #pointLight(255,0,127,0,0,0)
    popMatrix()
    # pop matrix of p2
    popMatrix()
    
    # display p3
    pushMatrix()
    rotateZ(-frameCount/60.0)
    translate(350,0,0)
    for f in planet3.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
    popMatrix()
    
    # export every frame into an image
    if frameCount<100:
        saveFrame("export/####.png")
    

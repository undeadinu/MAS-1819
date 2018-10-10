add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import *

def setup():
    size(800,800,P3D)
    cam = PeasyCam(this,300)
    noStroke()

    global my_mesh
    b = Box(0,0,0,100,100,100)
    my_mesh = b.get_mesh()
    
    rp = RulePyramid()
    for i in range(4):
        my_mesh = rp.replace(my_mesh, 10-i*6)
        
def draw():
    background(70)
    rotateX(PI/3)
    rotateZ(frameCount/100.0)
    directionalLight(255,  0,127,   0, 0, -1)
    directionalLight(  0,127,255,  -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    for i,f in enumerate(my_mesh.faces):
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
        

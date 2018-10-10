add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import*

def setup():
    size(800,800,P3D)
    cam = PeasyCam(this,130)
    
    
    s = 30

    global my_mesh
    my_mesh = Mesh()
    b = Box(0,0,0, 50, 40, 60)
    my_mesh = b.get_mesh()
    
    
    
    # my_mesh.add_face(f1)
    # my_mesh.add_face(f2)
    # my_mesh.add_face(f3)
    # my_mesh.add_face(f4)
    # my_mesh.add_face(f5)
    # my_mesh.add_face(f6)
    #my_mesh.add_faces([f1,f2,f3,f4,f5,f6])
    
    rp = RulePyramid()
    for i in range(3):
        my_mesh = rp.replace(my_mesh, 10-i*3)
    
    print len(my_mesh.faces)
    #noStroke()
    #noFill()
    stroke(0,127,255)
    
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
        
add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import *
from io import *

def setup():
    size(800,800,P3D)
    cam = PeasyCam(this,300)
    
    global my_mesh
    b = Box(0,0,0,100,100,100)
    my_mesh = b.get_mesh()
    
    rp = RulePyramid()
    for i in range(1):
        my_mesh = rp.replace(my_mesh,10)

    rt = RuleTapered()
    for i in range(1):
        my_mesh = rt.replace(my_mesh,0.5, 10)
    
    print len(my_mesh.faces)
    
    global myshape
    myshape = get_pshape(my_mesh)
    
def draw():
    background(77)
    rotateX(PI/3)
    rotateZ(frameCount/100.0)
    shape(myshape)
    
    # for f in my_mesh.faces:
    #     beginShape()
    #     for n in f.nodes:
    #         vertex(n.x,n.y,n.z)
    #     endShape(CLOSE)
    

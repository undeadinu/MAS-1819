add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import *
from io import *
from combinations import *

import octree as oc

from marching_cubes_3d import marching_cubes_3d_single_cell
from utils_3d import Mesh,Tri,Quad

def setup():
    size(800,450,P3D)
    cam = PeasyCam(this,700)
    
    #strokeWeight(5)
    #noStroke()
    
    global s,c,t,b,s2, rb
    global u,ints,subtr
    global sh
    
    # create primitives
    s = Sphere(cx=80,cy=90,rad=130)
    s2 = Sphere(cx=-80,cy=-90,rad=170)
    c = Cylinder(r=180,h=250)
    t = Torus(raddonut=130, radpipe=60)
    b = Box(a=150,b=250,c=200)
    d = Dodecahedron(rad=150)
    rb = RBox(a=300,b=250,c=200,r=50)
    
    # create boolean combinations
    u = Union(s,s2)
    ints = Intersection(s,s2)
    subtr = Subtraction(rb,s2)
    
    mcmesh = Mesh()
    ot = oc.OcTree(Vector(0,0,0), 400.0)
    ot.set_level(5)
    ot.distobj = t
    ot.divide(ot.rootnode, mcmesh)
    
    sh = createShape()
    sh.beginShape(TRIANGLES)
    for f in mcmesh.faces:
        sh.vertex(mcmesh.verts[f.v1-1].x,mcmesh.verts[f.v1-1].y,mcmesh.verts[f.v1-1].z)
        sh.vertex(mcmesh.verts[f.v2-1].x,mcmesh.verts[f.v2-1].y,mcmesh.verts[f.v2-1].z)
        sh.vertex(mcmesh.verts[f.v3-1].x,mcmesh.verts[f.v3-1].y,mcmesh.verts[f.v3-1].z)
    sh.endShape()
        
def draw():
    background(77)
    directionalLight(255,  0,127, 0,0,-1)
    directionalLight(  0,127,255, -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    shape(sh)
    
    """
    res = 10
    for x in range(-200,200,res):
        for y in range(-200,200,res):
            for z in range(-200,200,res):
                d = t.get_distance(x,y,z)
                
                # calculate fill color
                # col = color(0,d,0)
                # if d<0:
                #     col = color(-d,0,0)
                
                #if abs(d)<res:
                if d<0:
                    pushMatrix()
                    translate(x,y,z)
                    box(res)
                    popMatrix()
    """
    """
    lights()
    
    pushMatrix()
    rotate(TWO_PI*0/5.0)
    translate(400,0)
    shape(ss)
    popMatrix()
    
    pushMatrix()
    rotate(TWO_PI*1/5.0)
    translate(400,0)
    shape(cs)
    popMatrix()
    
    pushMatrix()
    rotate(TWO_PI*2/5.0)
    translate(400,0)
    shape(ts)
    popMatrix()
    
    pushMatrix()
    rotate(TWO_PI*3/5.0)
    translate(400,0)
    shape(bs)
    popMatrix()
    
    pushMatrix()
    rotate(TWO_PI*4/5.0)
    translate(400,0)
    shape(ds)
    popMatrix()
    """

def keyPressed():
    saveFrame("####.png")

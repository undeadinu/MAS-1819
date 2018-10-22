add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import *
from io import *
from combinations import *
from modifications import *

import octree as oc

from marching_cubes_3d import marching_cubes_3d_single_cell
from utils_3d import Mesh,Tri,Quad

def setup():
    size(800,450,P3D)
    cam = PeasyCam(this,700)
    
    #strokeWeight(5)
    noStroke()
    
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
    rb = RBox(a=150,b=250,c=200,r=50)
    
    # create boolean combinations
    u = Union(s,t)
    bl = Blend(s,t,r=30)
    ints = Intersection(s,s2)
    subtr = Subtraction(s,s2)
    
    shell = Shell(bl,20,1)
    subtr = Subtraction(shell,rb)
    
    mcmesh = Mesh()
    ot = oc.OcTree(Vector(0,0,0), 450.0)
    ot.set_level(7)
    ot.distobj = subtr
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
    

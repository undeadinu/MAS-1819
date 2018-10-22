add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *
from primitives import *
from io import *

def setup():
    size(800,450,P3D)
    cam = PeasyCam(this,700)
    
    global sm, ss, tm, ts, cm, cs, dm, ds, bm, bs
    s = Sphere(rad=180)
    c = Cylinder(r=180,h=250)
    t = Torus(raddonut=170, radpipe=60)
    b = Box(a=150,b=250,c=200)
    d = Dodecahedron(rad=150)
    
    sm = s.get_mesh()
    cm = c.get_mesh()
    tm = t.get_mesh()
    bm = b.get_mesh()
    dm = d.get_mesh()
    
    ss = get_pshape(sm)
    cs = get_pshape(cm)
    ts = get_pshape(tm)
    bs = get_pshape(bm)
    ds = get_pshape(dm)
        
def draw():
    background(255)
    rotateX(PI/3.5)
    rotateZ(frameCount/100.0)
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

def keyPressed():
    saveFrame("####.png")

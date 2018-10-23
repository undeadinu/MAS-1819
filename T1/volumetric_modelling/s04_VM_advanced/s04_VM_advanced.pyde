add_library('peasycam')

from meshobjs import *
from rules import *
from primitives import *
from io import *
from combinations import *
from modifications import *
import octree as oc

def setup():
    size(800,450,P3D)
    cam = PeasyCam(this,700)
    
    #strokeWeight(5)
    noStroke()
    
    global ix, dobjs, st, bt, sh
    ix = 0
    dobjs = []
    st = Sphere(40,40,40,150)
    bt = RBox(-50,-50,-50,280,280,280,40)
    dobjs.append(StairUnion(bt,st))
    dobjs.append(StairIntersection(bt,st))
    dobjs.append(StairSubtraction(bt,st))
    dobjs.append(ChamferUnion(bt,st))
    dobjs.append(ChamferIntersection(bt,st))
    dobjs.append(ChamferSubtraction(bt,st))
    dobjs.append(Pipe(bt,st))
    dobjs.append(UGroove(bt,st))
    dobjs.append(UGroove(bt,st,pos=True))
    dobjs.append(VGroove(bt,st))
    dobjs.append(VGroove(bt,st,pos=True))
    dobjs.append(Twist(bt,PI/2))
    dobjs.append(Taper(bt,30))
    
    recalc_geom(dobjs[ix])


def draw():
    background(77)
    rotateX(PI/3)
    directionalLight(255,  0,127,  0,  0,  -1)
    directionalLight(  0,127,255,  -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    shape(sh)


def recalc_geom(dobj):
    global sh
    mcmesh = Mesh()
    ot = oc.OcTree(Vector(0,0,0), 400.0)
    ot.set_level(7)
    ot.distobj = dobj
    ot.divide(ot.rootnode, mcmesh)
    sh = get_pshape(mcmesh)


def keyPressed():
    global ix
    n = len(dobjs)
    if key=='q':
        ix = (ix+1)%n
    elif key =='a':
        ix = (ix-1)%n
        
    recalc_geom(dobjs[ix])

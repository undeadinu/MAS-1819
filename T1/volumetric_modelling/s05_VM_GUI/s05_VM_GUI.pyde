add_library('controlP5')
add_library('peasycam')

from meshobjs import *
from rules import *
from primitives import *
from io import *
from combinations import *
from modifications import *
import octree as oc
from microstructures import *

def setup():
    size(1200,675,P3D)
    
    global cam, cp5, tf
    cam = PeasyCam(this,700)
    global ix, dobjs, st, bt, sh, mcmesh
    global sl # subdivision level
    sl = 3
    
    cp5 = ControlP5(this)
    cp5.addButton("<").addCallback(decrease).setSize(20,20).setPosition(20,20)
    tf = cp5.addLabel('val').setText(str(sl)).setPosition(55,25)
    cp5.addButton(">").addCallback(increase).setSize(20,20).setPosition(80,20)
    cp5.setAutoDraw(False)
    
    #strokeWeight(5)
    noStroke()
    
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
    dobjs.append(Intersection(Gyroid(w=60),bt))
    dobjs.append(Intersection(Diamond(w=60),bt))
    dobjs.append(Intersection(SchwartzP(w=60),bt))
    dobjs.append(Intersection(Shell(Gyroid(w=80),d=1.0,s=0.5),bt))
    dobjs.append(Intersection(FischerKoch(w=80),bt))

    # gyr = Gyroid(w=80)
    # shell = Shell(gyr,d=1.0,s=0.5)
    # ints = Intersection(shell,bt)
    # dobjs.append(ints)
    
    recalc_geom(dobjs[ix])


def draw():
    background(77)
    #rotateX(PI/3)
    directionalLight(255,  0,127,  0,  0,  -1)
    directionalLight(  0,127,255,  -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    shape(sh)
    
    gui()


def gui():
    hint(DISABLE_DEPTH_TEST);
    cam.beginHUD();
    cp5.draw();
    cam.endHUD();
    hint(ENABLE_DEPTH_TEST);

def increase(e):
    global sl
    if e.getAction()==ControlP5.RELEASED:
        sl += 1
        tf.setText(str(sl))
        recalc_geom(dobjs[ix])
    
def decrease(e):
    global sl
    if e.getAction()==ControlP5.RELEASED:
        sl -= 1
        tf.setText(str(sl))
        recalc_geom(dobjs[ix])

def recalc_geom(dobj):
    global sh,mcmesh,sl
    mcmesh = Mesh()
    ot = oc.OcTree(Vector(0,0,0), 400.0)
    ot.set_level(sl)
    ot.distobj = dobj
    ot.divide(ot.rootnode, mcmesh)
    sh = get_pshape(mcmesh)


def keyPressed():
    global ix,mcmesh,sl
    n = len(dobjs)
    if key=='q':
        ix = (ix+1)%n
        recalc_geom(dobjs[ix])
    elif key =='a':
        ix = (ix-1)%n
        recalc_geom(dobjs[ix])
    elif key=='w':
        sl += 1
        recalc_geom(dobjs[ix])
    elif key=='s':
        sl = max(0,sl-1)
        recalc_geom(dobjs[ix])
    elif key =='e':
        export_obj(mcmesh,'accuracy_test.obj')

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
    noStroke()

    global cam, cp5, tf
    cam = PeasyCam(this,500)
    global sh, mcmesh, dobjs, ix
    global sl # subdivision level
    global il
    il = 0
    sl = 5
    ix = 0
    dobjs = []
    
    plns = []
    # for i in range(50):
    #     p = PVector.random3D()
    #     plns.append(Plane(p.x,p.y,p.z,190.0))
    
    theta = TWO_PI/6
    mysin = Sinus(w=240,hb=100,ht=170,off=120)
    for i in range(6):
        x = cos(i*theta)
        y = sin(i*theta)
        plns.append(Plane(x,y,0.3,130))
        # tr = Transform(mysin)
        # tr.m.rotateX(-HALF_PI)
        # tr.m.rotateY(i*theta)
        # tr.m.rotateX(-0.2)
        # plns.append(tr)
    plns.append(Plane(0,0,1,100))
    plns.append(Plane(0,0,-1,100))
    #plns.append(Subtraction(Sphere(0,0,-500,600), Sphere(0,0,-500,400)))
    diamond = Intersection(plns)
    
    lat = Gyroid(w=40)
    shl = Shell(diamond,d=20,s=1)
    
    tp = Plane(0,0,1,75)
    bp = Plane(0,0,-1,75)
    tp2 = Plane(0,0,1,70)
    bp2 = Plane(0,0,-1,70)
    ints = Intersection([diamond,lat,tp2,bp2])
    ts = Intersection([shl,tp,bp])
    dobjs.append(ts)
    dobjs.append(Union(ts,Gradient(ints, Cylinder(0,0,0,100,500), f=-0.01)))

    dobjs.append(shl)
    dobjs.append(ints)
    
    sn = Sinus(w=400,hb=-100,ht=100,off=200)
    #dobjs.append(Intersection(Shell(sn,d=20,s=0.5),Sphere(rad=190)))
    dobjs.append(Intersection(sn,Sphere(rad=190)))
    
    dobjs.append(Dodecahedron(rad=190))
    dobjs.append(Gradient(Dodecahedron(rad=190),Gyroid(w=40),f=3))
    
    to = Torus(raddonut=100,radpipe=80)
    pl = Plane(1,1,0,0)
    dobjs.append(Gradient(to,pl))
    
    bx = Box(a=390,b=390,c=60)
    gy = Gyroid(w=30.0)
    ints = Intersection(bx,gy)
    dobjs.append(ints)
    cy = Cylinder(r=150,h=200)
    dobjs.append(Gradient(ints,cy,f=0.01))
    dobjs.append(Gradient(ints,pl,f=0.005))
    
    cp5 = ControlP5(this)
    cp5.addButton("<").addCallback(decrease).setSize(20,20).setPosition(20,20)
    tf = cp5.addLabel('val').setText(str(sl)).setPosition(55,25)
    cp5.addButton(">").addCallback(increase).setSize(20,20).setPosition(80,20)
    
    cp5.addSlider("sphere radius").addCallback(adjust_level)\
    .setRange(-200,200)\
    .setValue(il)\
    .setPosition(20,60)
    
    cp5.setAutoDraw(False)

    recalc_geom(dobjs[ix])

def draw():
    background(77)
    #rotateX(PI/3)
    # directionalLight(255,  0,127,  0,  0,  -1)
    # directionalLight(  0,127,255,  -1, 0, 0.3)
    # directionalLight(127,255,  0, 0.5, 1, 0.3)
    # directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    pushMatrix()
    translate(0,0,il)
    image(pic,-200,-200,400,400)
    popMatrix()
    lights()
    
    #shape(sh)
    
    stroke(255)
    noFill()
    box(400)
    
    gui()


def gui():
    # deactivates camera control for leftmost 200 pixels
    if mouseX<200:
        cam.setActive(False)
    else:
        cam.setActive(True)
        
    hint(DISABLE_DEPTH_TEST)
    cam.beginHUD()
    cp5.draw()
    cam.endHUD()
    hint(ENABLE_DEPTH_TEST)

def increase(e):
    global sl
    if e.getAction()==ControlP5.ACTION_RELEASE:
        sl += 1
        tf.setText(str(sl))
        recalc_geom(dobjs[ix])
    
def decrease(e):
    global sl
    if e.getAction()==ControlP5.ACTION_RELEASE:
        sl -= 1
        tf.setText(str(sl))
        recalc_geom(dobjs[ix])
        
# def adjust_radius(e):
#     global st
#     if e.getAction()==ControlP5.ACTION_RELEASE or e.getAction()==ControlP5.ACTION_RELEASEDOUTSIDE:
#         st.r = e.getController().getValue()
#         recalc_geom(dobjs[ix])

def adjust_level(e):
    global il
    if e.getAction()==ControlP5.ACTION_RELEASE or e.getAction()==ControlP5.ACTION_RELEASEDOUTSIDE:
        il = e.getController().getValue()
        recalc_geom(dobjs[ix])

def recalc_geom(dobj):
    global sh,mcmesh,sl, pic
    # mcmesh = Mesh()
    # ot = oc.OcTree(Vector(0,0,0), 400.0)
    # ot.set_level(sl)
    # ot.distobj = dobj
    # ot.divide(ot.rootnode, mcmesh)
    # sh = get_pshape(mcmesh)

    pic = get_image(dobj, ws=400.0, res=2.0, level=il)


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

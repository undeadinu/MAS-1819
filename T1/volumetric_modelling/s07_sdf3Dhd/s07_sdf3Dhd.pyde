add_library('peasycam')
add_library('HDGeo')

def setup():
    global rot,cam
    size(800,450,P3D)
    cam = PeasyCam(this,100)
    rot = 0
    noStroke()
    #fill(255,0,127)

def draw():
    background(77)
    directionalLight(255,  0,127,  0,  0,  -1)
    directionalLight(  0,127,255,  -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    global rot
    rot += 0.03
    gen_geo(rot)
    
    cam.beginHUD()
    noLights()
    #fill(0)
    text(frameRate,20,20)
    #fill(255,0,127)
    cam.endHUD()
    
def gen_geo(rt):
    sph = Sphere(0, 0, 0, 40)
    bx = VBox(-20, -20, -20, 20, 20, 20, 3)
    tw = CSGFRepTwist(bx,0.5,0)
    transform = CSGTransform(tw)
    transform.rotateZ(rt)
    transform.translate(20, 20, 20)
    transform.rotateX(rt)
    #combine = CSGBoolSubtract(sph, transform)
    combine = CSGBlend(sph, transform, 30)
    tree = P5OcTree(Point(0, 0, 0), 128)
    tree.divideForPGraphics(combine,6,g)
    

add_library('peasycam')
add_library('HDGeo')

import java.util.ArrayList as ArrayList

def setup():
    global rot,cam,hdmesh, renderer, num
    
    renderer = P5Renderer(g)
    size(800,450,P3D)
    cam = PeasyCam(this,100)
    rot = 0
    noStroke()
    #fill(255,0,127)
    num = 5
    hdmesh = gen_geo(num)

def draw():
    background(77)
    directionalLight(255,  0,127,  0,  0,  -1)
    directionalLight(  0,127,255,  -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    #global rot
    #rot += 0.03
    #gen_geo(rot)
    
    renderer.display3D(hdmesh)
    
    cam.beginHUD()
    noLights()
    #fill(0)
    text(frameRate,20,20)
    #fill(255,0,127)
    cam.endHUD()
    
def gen_geo(n):
    my_pts = ArrayList()
    theta = TWO_PI/(n*2)
    for i in range(n*2):
        r = 20 + (i%2)*20
        
        x = r*cos(i*theta)
        y = r*sin(i*theta)
        my_pts.add(Point(x,y,0))
        
    ext = Extrusion(my_pts,100)
    
    tr = OcTree(Point(0, 0, 0), 128)
    tr.csgSolid = ext
    tr.divideForMesh(tr.root,128)
    return tr.mesh
    
    # MeshToOBJ.saveMeshAsOBJ(tr.mesh,"/Users/bernham/Desktop/star.obj")
    
def keyPressed():
    global num, hdmesh
    if key=='q':
        num+=1
        hdmesh = gen_geo(num)
    if key=='a':
        num=max(num-1,2)
        hdmesh = gen_geo(num)
    

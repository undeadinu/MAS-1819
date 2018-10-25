add_library('peasycam')
add_library('HDGeo')

def setup():
    size(800,450,P3D)
    cam = PeasyCam(this,100)
    noStroke()
    
    global mesh
    # gyroid
    f = 0.3
    vals = [sin(x*f)*cos(y*f)+sin(y*f)*cos(z*f)+sin(z*f)*cos(x*f) for x in range(20) for y in range(30) for z in range(40)]
    #vals = [random(-1,1) for _ in range(20*30*40)]
    vs = VoxelSpace(vals,20,30,40)
    vtm = VoxelToMesh()
    mesh = vtm.getMesh(vs,0)
    
    global renderer
    renderer = P5Renderer(g)
    
def draw():
    background(77)
    directionalLight(255,  0,127,  0,  0,  -1)
    directionalLight(  0,127,255,  -1, 0, 0.3)
    directionalLight(127,255,  0, 0.5, 1, 0.3)
    directionalLight(  0,255,127, 0.5,-1, 0.3)
    
    renderer.display3D(mesh)

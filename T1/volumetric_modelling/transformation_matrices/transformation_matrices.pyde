def setup():
    global source_poly, target_poly
    source_poly = [
                   PVector(-100,-100,0),
                   PVector(-150,100,0),
                   PVector(150,150,0),
                   PVector(100,-150,0)
                   ]
    
    m = PMatrix3D()
    m.rotateZ(1)
    m.translate(200,0,0)
    m.rotateZ(-1)
    #m.translate(200*cos(1),200*sin(1),0)
    #m.scale(2.5)
    m.print()
    
    target_poly = [PVector(0,0,0) for _ in range(4)]
    target_poly = [PVector(0,0,0), PVector(0,0,0),PVector(0,0,0),PVector(0,0,0)]
    print target_poly
    for i in range(4):
        sv = source_poly[i]
        tv = target_poly[i]
        m.mult(sv,tv)
        #target_poly[i] = m.mult(sv,None)
    
    print target_poly    
    
    size(800,800)
    noFill()
    
def draw():
    background(255)
    translate(width/2,height/2)
    
    stroke(255,0,0)
    beginShape()
    for p in source_poly:
        vertex(p.x,p.y)
    endShape(CLOSE)
    
    stroke(0,0,255)
    beginShape()
    for p in target_poly:
        vertex(p.x,p.y)
    endShape(CLOSE)
    
    stroke(0)
    line(-100,0,100,0)
    line(0,-100,0,100)

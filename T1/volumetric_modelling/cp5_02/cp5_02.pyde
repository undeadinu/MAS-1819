add_library('peasycam')
add_library('controlP5')

def setup():
    size(800,450,P3D)

    global cp5, cam
    cam = PeasyCam(this,200)
    
    cp5 = ControlP5(this)
    cp5.addNumberbox("numberbox 1")\
    .setRange(0,255)\
    .setPosition(20,20)
    
    cp5.addNumberbox("numberbox 2")\
    .setRange(0,255)\
    .setPosition(20,60)
    
    cp5.addNumberbox("numberbox 3")\
    .setRange(0,255)\
    .setPosition(20,100)
    
    # myfont = createFont("Arial",18,False)
    # cp5.addNumberbox("numberbox 2")\
    #      .setFont(ControlFont(myfont))\
    #      .setSize(120,25)\
    #      .setRange(-10,10)\
    #      .setValue(7)\
    #      .setMultiplier(0.1)
    # nb3 = cp5.addNumberbox("third one")
    # nb3.setPosition(200,200)
    # nb3.setSize(300,30)
    # nb3.setColorValue(color(255,255,0))
    cp5.setAutoDraw(False)
    
def draw():
    val = cp5.getController("numberbox 1").getValue()
    background(val)
    fill(255,127,0)
    rect(60,60,600,300)
    
    if mouseX<150:
        cam.setActive(False)
    else:
        cam.setActive(True)
        
    # start 2d drawing on heads up display
    cam.beginHUD()
    fill(0,50)
    rect(0,0,150,height)
    cp5.draw()
    cam.endHUD()
    
    box(100)

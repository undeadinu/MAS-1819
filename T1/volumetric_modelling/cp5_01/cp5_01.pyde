add_library('controlP5')

def setup():
    size(800,450)
    
    global cp5
    cp5 = ControlP5(this)
    cp5.addNumberbox("numberbox 1").setRange(0,255)
    
    myfont = createFont("Arial",18,False)
    cp5.addNumberbox("numberbox 2")\
         .setFont(ControlFont(myfont))\
         .setSize(120,25)\
         .setRange(-10,10)\
         .setValue(7)\
         .setMultiplier(0.1)
    nb3 = cp5.addNumberbox("third one")
    nb3.setPosition(200,200)
    nb3.setSize(300,30)
    nb3.setColorValue(color(255,255,0))
    
def draw():
    val = cp5.getController("numberbox 1").getValue()
    background(val)

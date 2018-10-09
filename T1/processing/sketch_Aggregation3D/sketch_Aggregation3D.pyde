'''
ETH MAS DFAB 2018/19
Random Aggregation - tutorial written by Patrick Bedarf
Digital Building Technologies

References:
https://en.wikipedia.org/wiki/Diffusion-limited_aggregation
https://www.openprocessing.org/sketch/154495
Lomas, A. (2005) "Aggregation: Complexity out of Simplicity"
'''

add_library('peasycam')
from peasy import PeasyCam

def setup():
    global seeds
    size(800, 800, OPENGL)
    cam = PeasyCam(this, 200)
  
    seeds = []
    s = Seed(PVector(0,0,0))
    seeds.append(s)
        
def draw():
    background(50)
    smooth()
    #sphereDetail(9)
    
    directionalLight(155,155,155, 1, 1, 1)
    ambientLight(100, 100, 100)
    

    if frameCount % 1 == 0:
        addSeed()
    
    for s in seeds:
        s.display()    
    
def addSeed():
    if len(seeds) > 0:
        # points from sphere
        angleA = random(0, PI)
        angleB = random(0, TWO_PI)
        newVec = PVector(500*sin(angleA)*cos(angleB), 500*sin(angleA)*sin(angleB), 500*cos(angleA))
        
        # finding closest particle in aggregation
        newR = random(2, 50)
        closestDist = 100000000
        closestIndex = 0
        
        for i in range(len(seeds)):
            distance = PVector.dist(newVec, seeds[i].loc)
            if distance < closestDist:
                closestDist = distance
                closestIndex = i

        # calculating new location        
        newLoc = PVector.sub(seeds[closestIndex].loc, newVec)
        newLoc.normalize()
        newLoc.mult(-newR)
        newLoc.add(seeds[closestIndex].loc)
        
        # instantiating seed object
        newSeed = Seed(PVector(newLoc.x, newLoc.y, newLoc.z))
        newSeed.r = newR
        seeds.append(newSeed)
 
class Seed:
    def __init__(self, v):
        self.loc = PVector(v.x, v.y, v.z)
        self.r = 2
        self.c = color(millis()/50, 100, 100)
    
    def display(self):
        noStroke()
        fill(self.c)
        pushMatrix()
        translate(self.loc.x, self.loc.y, self.loc.z)
        sphere(self.r)
        popMatrix()    

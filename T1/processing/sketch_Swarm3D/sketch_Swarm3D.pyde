'''
ETH MAS DFAB 2018/19
Swarm 3D - tutorial written by Patrick Bedarf
Digital Building Technologies

References:
https://natureofcode.com/book/chapter-6-autonomous-agents/
Renolds, C. (1987) "Flocks, herds and schools: A distributed behavioral model"
Hymes, C., Klemmt, C. (2018) "Discrete Swarm Logics"
'''

add_library('peasycam')

def setup():
    global swarm, sep, ali, coh, maxF, maxS, record
    size(800, 800, OPENGL)
    cam = PeasyCam(this, 200)
    
    sep = 100
    ali = 10
    coh = 0
    maxF = 0.05
    maxS = 0.25
    
    swarm = []
    for i in range(100):
        b = Boid(random(-20, 20), random(-20, 20), 0, color(random(255), random(255), 200))
        swarm.append(b)
    
def draw():
    background(50)
    smooth()
    
    # boundary box
    noFill()
    stroke(0)
    box(50, 50, 200)
    
    for boid in swarm:
        boid.run()

class Boid:
    def __init__(self, x, y, z, col):
        self.x = x
        self.y = y
        self.z = z
        self.locList = []
        self.col = col
        
        self.loc = PVector(self.x, self.y, self.z)
        self.acc = PVector(0, 0, 0)
        self.vel = PVector(random(-1, 1), random(-1, 1), random(-1, 1))
        
    def run(self):
        self.flock()
        self.update()
        self.borders()
        self.display()
        self.displayTrail()
    
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(maxS)
        self.loc.add(self.vel)
        self.acc.mult(0)
    
    def flock(self):
        force = self.separate(swarm)    # calc force
        force.mult(0.01 * sep)          # global multiplier
        self.acc.add(force)             # apply force
        
        force = self.align(swarm)
        force.mult(0.01 * ali)
        self.acc.add(force)
        
        force = self.cohesion(swarm)
        force.mult(0.01 * coh)
        self.acc.add(force)
        
        # optional attract target
        # force = self.attract(PVector(0, 0, 50))
        # self.acc.add(force)
        
    def attract(self, target):          # optional
        steer = self.seek(target)
        steer.mult(maxF)
        return steer

    def separate(self, boids):
        desiredseparation = 10
        count = 0
        sum = PVector(0, 0, 0)
        for other in boids:
            d = PVector.dist(self.loc, other.loc)
            if ((d > 0) and (d < desiredseparation)): 
                diff = PVector.sub(self.loc, other.loc) 
                diff.normalize()
                diff.div(d)             # the closer the stronger
                sum.add(diff) 
                count += 1
        if (count > 0): 
            sum.div(count) 
            sum.normalize()
            sum.mult(maxS)
            sum.sub(self.vel) 
            sum.limit(maxF)
        return sum
    
    def align(self, boids):
        neighbordist = 20 
        sum = PVector(0, 0, 0)
        count = 0
        for other in boids:
            d = PVector.dist(self.loc, other.loc)
            if ((d > 0) and (d < neighbordist)):
                sum.add(other.vel) 
                count += 1
        if (count > 0):
            sum.div(count) 
            sum.normalize()
            sum.mult(maxS)
            steer = PVector.sub(sum, self.vel) 
            steer.limit(maxF)
            return steer
        else:
            return PVector(0, 0, 0) 
    
    def cohesion(self, boids):
        neighbordist = 20
        sum = PVector(0, 0, 0)
        count = 0
        for other in boids:
            d = PVector.dist(self.loc, other.loc)
            if((d > 0) and (d < neighbordist)):
                sum.add(other.loc) 
                count += 1
        if (count > 0):
            sum.div(count) 
            return self.seek(sum) 
        else:
            return PVector(0, 0, 0)
        
    def seek(self, target):
        desired = PVector.sub(target, self.loc)     # desired velocity
        desired.normalize()
        desired.mult(maxS)                          # at max speed
        steer = PVector.sub(desired, self.vel)      # Reynolds steering formula
        steer.limit(maxF)                           # limit max force
        return steer
      
    def display(self):
        stroke(self.col)
        strokeWeight(5)
        point(self.loc.x, self.loc.y, self.loc.z)
    
    def displayTrail(self):
        # record trail loc
        if (millis() % 10) == 0:
            recLoc = self.loc.copy()
            # snapping recLoc to 5x5x5 grid
            # recLoc.set(round(recLoc.x/5)*5, round(recLoc.y/5)*5, round(recLoc.z/5)*5)
            self.locList.append(recLoc)
            
        # display
        beginShape()
        strokeWeight(0.5)
        stroke(self.col)
        noFill()
        for i in range(1, len(self.locList)):
            # version with lines for export
            # line(self.locList[i].x, self.locList[i].y, self.locList[i].z, self.locList[i-1].x, self.locList[i-1].y, self.locList[i-1].z)
            v = self.locList[i]
            vertex(v.x, v.y, v.z)
        endShape()
           
    def borders(self):
        if (self.loc.x < -50/2) or (self.loc.x > 50/2): self.vel.x *= -1
        if (self.loc.y < -50/2) or (self.loc.y > 50/2): self.vel.y *= -1
        if (self.loc.z < -200/2) or (self.loc.z > 200/2): self.vel.mult(0)

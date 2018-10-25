import math

class TPMS(object):
    def __init__(self, w=10.0):
        self.wl = w*0.5
        self.fact = (math.pi)/w
        
    def get_distance(self,x,y,z):
        px = x*self.fact
        py = y*self.fact
        pz = z*self.fact
        return self.get_value(px,py,pz) #*self.wl
    
    def get_value(self,x,y,z):
        return 0
        
class Gyroid(TPMS):
    def get_value(self,px,py,pz):
        return math.sin(px)*math.cos(py) + math.sin(py)*math.cos(pz) + math.sin(pz)*math.cos(px)
    
class SchwartzP(TPMS):
    def get_value(self,px,py,pz):
        return math.cos(px)+math.cos(py)+math.cos(pz)
    
class Diamond(TPMS):
    def get_value(self,px,py,pz):
        return (
            math.sin(px) * math.sin(py) * math.sin(pz) + 
            math.sin(px) * math.cos(py) * math.cos(pz) + 
            math.cos(px) * math.sin(py) * math.cos(pz) +
            math.cos(px) * math.cos(py) * math.sin(pz))
        
class FischerKoch(TPMS):
    def get_value(self,px,py,pz):
        return (
            math.cos(2*px) * math.sin(py) * math.cos(pz) +
            math.cos(2*py) * math.sin(pz) * math.cos(px) +
            math.cos(2*pz) * math.sin(px) * math.cos(py))

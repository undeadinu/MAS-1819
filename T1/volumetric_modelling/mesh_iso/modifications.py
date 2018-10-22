class Shell(object):
    """
    creates a shell of thickness d
    side factor s:
        1 > inside
        0.5 > half half
        0 > outside
    """
    
    def __init__(self, obj, d=1, s=0):
        self.o = obj
        self.d = d
        self.s = s
        
    def get_distance(self,x,y,z):
        do = self.o.get_distance(x,y,z)
        # half half
        #return abs(do)-self.d/2.0
        return abs(do + (self.s-0.5)*self.d)-self.d/2.0

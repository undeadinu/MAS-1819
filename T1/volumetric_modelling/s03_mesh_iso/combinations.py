class Union(object):
    """
    boolean union of two or more objects
    """
    def __init__(self, obja, objb):
        self.a = obja
        self.b = objb
        
    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        return min(da,db)
    
class Intersection(object):
    """
    boolean intersection of two or more objects
    """
    def __init__(self, obja, objb):
        self.a = obja
        self.b = objb
        
    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        return max(da,db)
    
class Subtraction(object):
    """
    boolean subtraction of a minus b
    """
    def __init__(self, obja, objb):
        self.a = obja
        self.b = objb
        
    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        return max(da,-db)
    
class Blend(object):
    """
    smooth blend between a and b
    """
    def __init__(self, obja, objb, r=2):
        self.a = obja
        self.b = objb
        self.r = r
        
    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        e = max(self.r - abs(da-db), 0)
        return min(da,db) - e*e*0.25/self.r
    

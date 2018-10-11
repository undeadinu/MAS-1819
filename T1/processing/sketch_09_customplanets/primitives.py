from meshobjs import *

class Box(object):
    """
    this is the box class
    """
    def __init__(self, cx=0, cy=0, cz=0, a=1, b=1, c=1):
        self.loc = Vector(cx,cy,cz)
        self.a = a
        self.b = b
        self.c = c
        
    def get_mesh(self):
        m = Mesh()
        
        ha = self.a/2.0
        hb = self.b/2.0
        hc = self.c/2.0
        nodes = []
        nodes.append(Node(-ha,-hb,-hc))
        nodes.append(Node( ha,-hb,-hc))
        nodes.append(Node( ha, hb,-hc))
        nodes.append(Node(-ha, hb,-hc))
        nodes.append(Node(-ha,-hb, hc))
        nodes.append(Node( ha,-hb, hc))
        nodes.append(Node( ha, hb, hc))
        nodes.append(Node(-ha, hb, hc))
        
        for i in range(len(nodes)):
            vadd = nodes[i].addition(self.loc)
            nodes[i] = Node(vadd.x, vadd.y, vadd.z)
        
        m.add_face(Face([nodes[3],nodes[2],nodes[1],nodes[0]]))
        m.add_face(Face([nodes[4],nodes[5],nodes[6],nodes[7]]))
        m.add_face(Face([nodes[0],nodes[1],nodes[5],nodes[4]]))
        m.add_face(Face([nodes[2],nodes[3],nodes[7],nodes[6]]))
        m.add_face(Face([nodes[1],nodes[2],nodes[6],nodes[5]]))
        m.add_face(Face([nodes[4],nodes[7],nodes[3],nodes[0]]))
        return m
    
class Dodecahedron(object):
    """
    this is the dodecahedron class.
    a polyhedron made of 12 equilateral pentagons.
    """
    def __init__(self, cx=0, cy=0, cz=0, rad=1):
        self.loc = Vector(cx,cy,cz)
        self.rad = rad
        
    def get_mesh(self):
        m = Mesh()
        
        phi = (1+sqrt(5.0))/2.0
        nodes = []
        nodes.append(Node( 1, 1, 1))
        nodes.append(Node( 1, 1,-1))
        nodes.append(Node( 1,-1, 1))
        nodes.append(Node( 1,-1,-1))
        nodes.append(Node(-1, 1, 1))
        nodes.append(Node(-1, 1,-1))
        nodes.append(Node(-1,-1, 1))
        nodes.append(Node(-1,-1,-1))
        
        nodes.append(Node(0,-phi,-1/phi))
        nodes.append(Node(0,-phi, 1/phi))
        nodes.append(Node(0, phi,-1/phi))
        nodes.append(Node(0, phi, 1/phi))
    
        nodes.append(Node(-phi,-1/phi,0))
        nodes.append(Node(-phi, 1/phi,0))
        nodes.append(Node( phi,-1/phi,0))
        nodes.append(Node( phi, 1/phi,0))
        
        nodes.append(Node(-1/phi,0,-phi))
        nodes.append(Node( 1/phi,0,-phi))
        nodes.append(Node(-1/phi,0, phi))
        nodes.append(Node( 1/phi,0, phi))
        
        for i in range(len(nodes)):
            vadd = nodes[i].addition(self.loc)
            vadd = vadd.multiply(self.rad)
            nodes[i] = Node(vadd.x, vadd.y, vadd.z)
        
        m.add_face(Face([nodes[2], nodes[9], nodes[6], nodes[18], nodes[19]]))
        m.add_face(Face([nodes[4], nodes[11], nodes[0], nodes[19], nodes[18]]))
        m.add_face(Face([nodes[18], nodes[6], nodes[12], nodes[13], nodes[4]]))
        m.add_face(Face([nodes[19], nodes[0], nodes[15], nodes[14], nodes[2]]))
        m.add_face(Face([nodes[4], nodes[13], nodes[5], nodes[10], nodes[11]]))
        m.add_face(Face([nodes[14], nodes[15], nodes[1], nodes[17], nodes[3]]))
        m.add_face(Face([nodes[1], nodes[15], nodes[0], nodes[11], nodes[10]]))
        m.add_face(Face([nodes[3], nodes[17], nodes[16], nodes[7], nodes[8]]))
        m.add_face(Face([nodes[2], nodes[14], nodes[3], nodes[8], nodes[9]]))
        m.add_face(Face([nodes[6], nodes[9], nodes[8], nodes[7], nodes[12]]))
        m.add_face(Face([nodes[1], nodes[10], nodes[5], nodes[16], nodes[17]]))
        m.add_face(Face([nodes[12], nodes[7], nodes[16], nodes[5], nodes[13]]))
        
        return m

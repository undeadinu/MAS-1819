from meshobjs import*

class Box(object):
    
    """
    This is the box class
    
    """
    
    def __init__(self, cx=0 , cy=0, cz=0, a=1, b=1, c=1):
        self.loc = Vector(cx, cy, cz)
        self.a = a
        self.b = b
        self.c = c
        
        
    def get_mesh(self):
        
        m= Mesh()
        
        ha = self.a/2.0
        hb = self.b/2.0
        hc = self.c/2.0
        
        nodes= []
        
        nodes.append(Node (-ha, -hb, -hc))
        nodes.append(Node ( ha, -hb, -hc))
        nodes.append(Node ( ha,  hb, -hc))
        nodes.append(Node (-ha,  hb, -hc))
        
        nodes.append(Node (-ha, -hb,  hc))
        nodes.append(Node ( ha, -hb,  hc))
        nodes.append(Node ( ha,  hb,  hc))
        nodes.append(Node (-ha,  hb,  hc))
        
        for i in range(len(nodes)):
            nodes[i] = nodes[i].addition(self.loc)
            
            
        m.add_face(Face([nodes[3], nodes[2], nodes[1], nodes[0] ]))
        m.add_face(Face([nodes[4], nodes[5], nodes[6], nodes[7] ]))
        m.add_face(Face([nodes[0], nodes[1], nodes[5], nodes[4] ]))
        m.add_face(Face([nodes[2], nodes[3], nodes[7], nodes[6] ]))
        m.add_face(Face([nodes[1], nodes[2], nodes[6], nodes[5] ]))
        m.add_face(Face([nodes[4], nodes[7], nodes[3], nodes[0] ]))
        
        return m
        
        
        
        
        
        
class Node:
    """
    this is the node class.
    """
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "Node at {} {} {}".format(self.x,self.y,self.z)

class Face(object):
    """
    this is our face class.
    """
    def __init__(self, nodes=[]):
        self.nodes = nodes
        
    def add_node(self, n):
        self.nodes.append(n)
        
    def get_centroid(self):
        num = len(self.nodes)
        # xlist = []
        # for n in self.nodes:
        #     xlist.append(n.x)    
        # avx = sum(xlist)/num
        avx = sum([n.x for n in self.nodes])/num
        avy = sum([n.y for n in self.nodes])/num
        avz = sum([n.z for n in self.nodes])/num
        return Node(avx,avy,avz)

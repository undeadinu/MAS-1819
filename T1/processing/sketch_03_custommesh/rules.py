from meshobjs import *

class RulePyramid(object):
    """
    pyramid subdivision
    """
    def __init__(self):
        pass
        
    def replace(self, mesh):
        new_mesh = Mesh()
        for f in mesh.faces:
            center_node = f.get_centroid()
            for i in range(len(f.nodes)):
                n1 = f.nodes[i]
                n2 = f.nodes[(i+1) % len(f.nodes)]
                new_face = Face([n1,n2,center_node])
                new_mesh.add_face(new_face)
        return new_mesh

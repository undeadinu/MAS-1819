from meshobjs import *

class RulePyramid(object):
    """
    pyramid subdivision
    """
    def __init__(self):
        pass
        
    def replace(self, mesh, m):
        new_mesh = Mesh()
        for f in mesh.faces:
            center_node = f.get_centroid()
            # e1 = f.nodes[1].subtract(f.nodes[0])
            # e2 = f.nodes[-1].subtract(f.nodes[0])
            # face_normal = e1.cross_product(e2)
            # face_normal = f.get_normal()
            # unit_normal = face_normal.normalized()
            # move_vec = unit_normal.multiply(m)
            move_vec = f.get_normal_of_length(m)
            new_node = center_node.addition(move_vec)
            for i in range(len(f.nodes)):
                n1 = f.nodes[i]
                n2 = f.nodes[(i+1) % len(f.nodes)]
                new_face = Face([n1,n2,new_node])
                new_mesh.add_face(new_face)
        return new_mesh
    
class RuleTapered(object):
    """
    tapered subdivision. flag for center face.
    if height=0 equals to window subdivision.
    if distance factor df=0 equals to extrusion.
    """
    def __init__(self):
        pass
        
    def replace(self, mesh, h, df):
        new_mesh = Mesh()
        
        return new_mesh

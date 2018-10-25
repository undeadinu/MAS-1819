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
            scaled_normal = f.get_normal_of_length(m)
            np = center_node.addition(scaled_normal)
            new_node = Node(np.x,np.y,np.z)
            for i in range(len(f.nodes)):
                n1 = f.nodes[i]
                n2 = f.nodes[(i+1) % len(f.nodes)]
                new_face = Face([n1,n2,new_node])
                new_mesh.add_face(new_face)
        return new_mesh
    
class RuleTapered(object):
    """
    create a tapered extrude.
    distance factor df, 0 to 1.
    height h distance from original face.
    cap True or False for center face.
    """
    def __init__(self):
        pass
        
    def replace(self, mesh, df=0.5, h=0, cap=True):
        new_mesh = Mesh()
        for f in mesh.faces:
            center_node = f.get_centroid()
            scaled_normal = f.get_normal_of_length(h)
            
            # calculate new node positions
            new_nodes = []
            for i in range(len(f.nodes)):
                n1 = f.nodes[i]
                betw = center_node.subtract(n1)
                betw = betw.multiply(df)
                nn = n1.addition(betw)
                nn = nn.addition(scaled_normal)
                new_nodes.append(Node(nn.x,nn.y,nn.z))
                
            # create the quads along the edges
            for i in range(len(f.nodes)):
                n1 = f.nodes[i]
                n2 = f.nodes[(i+1) % len(f.nodes)]
                n3 = new_nodes[(i+1) % len(f.nodes)]
                n4 = new_nodes[i]
                new_face = Face([n1,n2,n3,n4])
                new_mesh.add_face(new_face)
               
            # create the closing cap face
            if cap:
                cap_face = Face(new_nodes)
                new_mesh.add_face(cap_face)
                
        return new_mesh

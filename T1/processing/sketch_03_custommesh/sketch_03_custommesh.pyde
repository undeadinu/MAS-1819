add_library('peasycam')

from meshobjs import Node, Face, Mesh
from rules import *

def setup():
    size(800,800,P3D)
    cam = PeasyCam(this,130)
    
    s = 30
    n1 = Node(-s,-s,-s)
    n2 = Node( s,-s,-s)
    n3 = Node( s, s,-s)
    n4 = Node(-s, s,-s)
    n5 = Node(-s,-s, s)
    n6 = Node( s,-s, s)
    n7 = Node( s, s, s)
    n8 = Node(-s, s, s)
    
    global node_list
    node_list = [n1,n2,n3,n4,n5,n6,n7,n8]
    
    # global face_list
    # face_list = []
    
    f1 = Face()
    f1.add_node(n1)
    f1.add_node(n2)
    f1.add_node(n3)
    f1.add_node(n4)
    #face_list.append(f)
    
    f2 = Face([n5,n6,n7,n8])
    #face_list.append(f2)
    
    f3 = Face([n5,n6,n2,n1])
    #face_list.append(f3)
    
    f4 = Face([n7,n8,n4,n3])
    #face_list.append(f4)
    
    f5 = Face([n2,n3,n7,n6])
    #face_list.append(f5)
    
    f6 = Face([n1,n4,n8,n5])
    #face_list.append(f6)
    
    global my_mesh
    my_mesh = Mesh()
    # my_mesh.add_face(f1)
    # my_mesh.add_face(f2)
    # my_mesh.add_face(f3)
    # my_mesh.add_face(f4)
    # my_mesh.add_face(f5)
    # my_mesh.add_face(f6)
    my_mesh.add_faces([f1,f2,f3,f4,f5,f6])
    
    rp = RulePyramid()
    for i in range(4):
        my_mesh = rp.replace(my_mesh)
    
    print len(my_mesh.faces)
    #noStroke()
    #noFill()
    stroke(0,127,255)
    
def draw():
    background(70)
    rotateX(PI/3)
    rotateZ(frameCount/100.0)
    #box(50)
    
    for f in my_mesh.faces:
        beginShape()
        for n in f.nodes:
            vertex(n.x,n.y,n.z)
        endShape(CLOSE)
        
        # centroid = f.get_centroid()
        # strokeWeight(15)
        # point(centroid.x,centroid.y,centroid.z)
        # strokeWeight(1)
        
    # for i,n in enumerate(node_list):
    #     text(str(i), n.x,n.y,n.z)
        
        
        
        
        
        
    # beginShape()
    # vertex(node_list[0].x,node_list[0].y, node_list[0].z)
    # vertex(node_list[1].x,node_list[1].y, node_list[1].z)
    # vertex(node_list[2].x,node_list[2].y, node_list[2].z)
    # vertex(node_list[3].x,node_list[3].y, node_list[3].z)
    # endShape()
    
    # beginShape()
    # vertex(node_list[4].x,node_list[4].y, node_list[4].z)
    # vertex(node_list[5].x,node_list[5].y, node_list[5].z)
    # vertex(node_list[6].x,node_list[6].y, node_list[6].z)
    # vertex(node_list[7].x,node_list[7].y, node_list[7].z)
    # endShape()
    
    # beginShape()
    # vertex(node_list[1].x,node_list[1].y, node_list[1].z)
    # vertex(node_list[2].x,node_list[2].y, node_list[2].z)
    # vertex(node_list[6].x,node_list[6].y, node_list[6].z)
    # vertex(node_list[5].x,node_list[5].y, node_list[5].z)
    # endShape()

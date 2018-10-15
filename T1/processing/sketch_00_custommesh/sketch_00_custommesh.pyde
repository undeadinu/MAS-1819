add_library('peasycam')

from meshobjs import Node

def setup():
    size(800,800,P3D)
    cam = PeasyCam(this,100)
    
    n1 = Node(-1,-1,-1)
    n2 = Node( 1,-1,-1)
    n3 = Node( 1, 1,-1)
    n4 = Node(-1, 1,-1)
    n5 = Node(-1,-1, 1)
    n6 = Node( 1,-1, 1)
    n7 = Node( 1, 1, 1)
    n8 = Node(-1, 1, 1)
    
    global node_list
    node_list = [n1,n2,n3,n4,n5,n6,n7,n8]
    
    #noStroke()
    
    stroke(0,127,255)
    strokeWeight(0.2)
    
def draw():
    background(70)
    #box(50)
    scale(50)
    
    beginShape()
    vertex(node_list[0].x,node_list[0].y, node_list[0].z)
    vertex(node_list[1].x,node_list[1].y, node_list[1].z)
    vertex(node_list[2].x,node_list[2].y, node_list[2].z)
    vertex(node_list[3].x,node_list[3].y, node_list[3].z)
    endShape()
    
    beginShape()
    vertex(node_list[4].x,node_list[4].y, node_list[4].z)
    vertex(node_list[5].x,node_list[5].y, node_list[5].z)
    vertex(node_list[6].x,node_list[6].y, node_list[6].z)
    vertex(node_list[7].x,node_list[7].y, node_list[7].z)
    endShape()
    
    beginShape()
    vertex(node_list[1].x,node_list[1].y, node_list[1].z)
    vertex(node_list[2].x,node_list[2].y, node_list[2].z)
    vertex(node_list[6].x,node_list[6].y, node_list[6].z)
    vertex(node_list[5].x,node_list[5].y, node_list[5].z)
    endShape()

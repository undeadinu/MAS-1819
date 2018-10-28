def export_obj(mesh,filename="output.obj"):
    out = createWriter(filename)
    out.println("# mesh exported from p5py by mathias")
    
    mesh.collect_nodes()
    
    for n in mesh.nodes:
        out.println("v {} {} {}".format(n.x,n.y,n.z))
        
    out.println("g triangles")
    tris = [f for f in mesh.faces if len(f.nodes)==3]
    for f in tris:
        index_list = [str(n.id) for n in f.nodes]
        out.println("f "+" ".join(index_list))

    out.println("g quads")
    quads = [f for f in mesh.faces if len(f.nodes)==4]
    for f in quads:
        index_list = [str(n.id) for n in f.nodes]
        out.println("f "+" ".join(index_list))
        
    out.flush()
    out.close()
    print "obj file successfully written"
    
def get_pshape(mesh):
    # create pshape object
    fill(255)
    noStroke()
    my_pshape = createShape(GROUP)
    
    # start adding triangular faces
    tris = [f for f in mesh.faces if len(f.nodes)==3]
    my_tris = createShape()
    my_tris.beginShape(TRIANGLES)
    for f in tris:
        for n in f.nodes:
            my_tris.vertex(n.x,n.y,n.z)
    my_tris.endShape()
    my_pshape.addChild(my_tris)
    
    # start adding quad faces
    quads = [f for f in mesh.faces if len(f.nodes)==4]
    my_quads = createShape()
    my_quads.beginShape(QUADS)
    for f in quads:
        for n in f.nodes:
            my_quads.vertex(n.x,n.y,n.z)
    my_quads.endShape()
    my_pshape.addChild(my_quads)
    
    # start adding other faces
    others = [f for f in mesh.faces if len(f.nodes)>4]
    for f in others:
        face = createShape()
        face.beginShape()
        for n in f.nodes:
            face.vertex(n.x,n.y,n.z)
        face.endShape(CLOSE)
        my_pshape.addChild(face)
    
    # return 1 pshape object
    return my_pshape

def get_image(dobj, ws=400.0, res=2.0, level=0):
    w = int(ws/res)
    h = w
    vals = []
    for j in range(h):
        for i in range(w):
            x = i*res-ws/2.0
            y = j*res-ws/2.0
            z = level
            vals.append(dobj.get_distance(x,y,z))
    mn = min(vals)
    mx = max(vals)
    
    pic = createImage(w,h,RGB)
    pic.loadPixels()
    for i in range(w*h):
        v = vals[i]
        if v<0:
            f = 1-v/mn
            col = color(255,f*255,127+f*128)
        else:
            f = 1-v/mx
            col = color(f*255,127+f*128,255)
        pic.pixels[i] = col
    return pic

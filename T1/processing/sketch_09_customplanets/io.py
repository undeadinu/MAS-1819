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

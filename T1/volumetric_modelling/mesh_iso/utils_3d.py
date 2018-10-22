"""Contains utilities common to 3d meshing methods"""

import math

class V3:
    """A vector in 3D space"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        d = math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        return V3(self.x / d, self.y / d, self.z / d)
    
    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)

class Tri:
    """A 3d triangle"""
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def map(self, f):
        return Tri(f(self.v1), f(self.v2), f(self.v3))


class Quad:
    """A 3d quadrilateral (polygon with 4 vertices)"""
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    def map(self, f):
        return Quad(f(self.v1), f(self.v2), f(self.v3), f(self.v4))

    def swap(self, swap=True):
        if swap:
            return Quad(self.v4, self.v3, self.v2, self.v1)
        else:
            return Quad(self.v1, self.v2, self.v3, self.v4)


class Mesh:
    """A collection of vertices, and faces between those vertices."""
    def __init__(self, verts=None, faces=None):
        self.verts = verts or []
        self.faces = faces or []

    def extend(self, other):
        l = len(self.verts)
        f = lambda v: v + l
        self.verts.extend(other.verts)
        self.faces.extend(face.map(f) for face in other.faces)

    def __add__(self, other):
        r = Mesh()
        r.extend(self)
        r.extend(other)
        return r

    def translate(self, offset):
        new_verts = [V3(v.x + offset.x, v.y + offset.y, v.z + offset.z) for v in self.verts]
        return Mesh(new_verts, self.faces)
    
    def weld_vertices(self):
        new_mesh = Mesh()
        #new_mesh.verts.append(mesh.verts[0])
        tol = 0.0001
        for j,f in enumerate(self.faces):
            #print j
            fn = Tri(f.v1,f.v2,f.v3)
            if isinstance(f, Quad):
                print "number %d is a quad" % j
                
            a = self.verts[f.v1-1]
            found = False
            for i,nv in enumerate(new_mesh.verts):
                if a.distance(nv)<tol:
                    fn.v1 = i+1
                    found = True
                    break
            if not found:
                new_mesh.verts.append(a)
                fn.v1 = len(new_mesh.verts)
                
            b = self.verts[f.v2-1]
            found = False
            for i,nv in enumerate(new_mesh.verts):
                if b.distance(nv)<tol:
                    fn.v2 = i+1
                    found = True
                    break
            if not found:
                new_mesh.verts.append(b)
                fn.v2 = len(new_mesh.verts)
                
            c = self.verts[f.v3-1]
            found = False
            for i,nv in enumerate(new_mesh.verts):
                if c.distance(nv)<tol:
                    fn.v3 = i+1
                    found = True
                    break
            if not found:
                new_mesh.verts.append(c)
                fn.v3 = len(new_mesh.verts)
                
            new_mesh.faces.append(fn)
        return new_mesh


def make_obj(f, mesh):
    """Crude export to Wavefront mesh format"""
    for v in mesh.verts:
        f.write("v {} {} {}\n".format(v.x, v.y, v.z))
    for face in mesh.faces:
        if isinstance(face, Quad):
            f.write("f {} {} {} {}\n".format(face.v1, face.v2, face.v3, face.v4))
        if isinstance(face, Tri):
            f.write("f {} {} {}\n".format(face.v1, face.v2, face.v3))

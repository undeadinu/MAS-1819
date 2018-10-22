"""Contains utilities common to all meshing methods"""

# Both marching cube and dual contouring are adaptive, i.e. they select
# the vertex that best describes the underlying function. But for illustrative purposes
# you can turn this off, and simply select the midpoint vertex.
ADAPTIVE = True

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def swap(self, swap=True):
        if swap:
            return Edge(self.v2, self.v1)
        else:
            return Edge(self.v1, self.v2)

def adapt(v0, v1):
    """v0 and v1 are numbers of opposite sign. This returns how far you need to interpolate from v0 to v1 to get to 0."""
    assert (v1 > 0) != (v0 > 0), "v0 and v1 do not have opposite sign"
    if ADAPTIVE:
        return (0 - v0) / (v1 - v0)
    else:
        return 0.5

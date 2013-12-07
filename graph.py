# coding: utf-8
"""
Author: Jerry Rong

Adjacency lists representations of graph
"""

class Graph(object):

    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].append((v1, v2))
        self.vertices[v2].append((v2, v1))
        self.edges.append((v1, v2))

    def get_vertices(self):
        return self.vertices.keys()

    def get_edges(self):
        return self.edges

    def __str__(self):
        """
        print each vertex in the graph with a list of vertices was connected
        """
        re = "Graph:\n"
        for v in self.vertices:
            re += "%s : %s\n" % (v, self.vertices[v])
        return re

# Some test for Graph class

def test():
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_edge(1,3)
    g.add_edge(1,2)
    g.add_edge(3,4)
    g.add_edge(2,5)
    print g.get_vertices()
    print g
    print g.get_edges()

if __name__ == "__main__":
    test()

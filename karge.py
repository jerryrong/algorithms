import re
import sys
import copy
import math
from random import randrange
 
G = []
mincut = sys.maxint
last_contracted_value = None
 
def find_vertex(G, val):
    for i in range(0, len(G)):
        if G[i][0] == val:
            return i
 
with open('kargerMinCut.txt', 'r') as f:
    for line in f:
        G.append([int(char) for char in re.split("\s+", line)[:-1]]) # note the tabs on the end of each line in sample file

def find_mincut(G):
    global mincut
 
    def contract(G, u, v):
        # Contract
        G[u] = G[u] + G[v][1:]
 
        # Substitute it in neighbours lists
        neighbours = G[v][1:]
 
        for neighbour in neighbours:
            ni = find_vertex(G, neighbour)
 
            for i in range(1, len(G[ni])):
                if G[ni][i] == G[v][0]:
                    G[ni][i] = G[u][0]
 
        # Remove self-loops
        G[u] = [G[u][0]] + filter(lambda x: x != G[u][0], G[u])
 
        del G[v]
 
        return G
 
    while len(G) > 2:
        u = randrange(0, len(G))
 
        neighbours = G[u][1:]
 
        while True:
            v = randrange(0, len(neighbours)) # in neighbours' array
            v = find_vertex(G, neighbours[v])
 
            if u != v:
                break
 
        G = contract(G, u, v)
 
    cut = len(G[0])-1
 
    if cut < mincut:
        mincut = cut
 
iterations = int(pow(len(G), 2) * math.log(len(G)))
 
for i in range(0, iterations+1):
    if i % 10 == 0:
        print "iteration {}, mincut: {}".format(i, mincut)
    find_mincut(copy.deepcopy(G))
 
print "MinCut: {}".format(mincut)

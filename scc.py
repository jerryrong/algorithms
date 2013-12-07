# coding: utf-8
import sys
import resource
import heapq # http://docs.python.org/2/library/heapq.html
import time
 
start = time.time()
 
resource.setrlimit(resource.RLIMIT_STACK, (2**29, 2**30))
sys.setrecursionlimit(10**6)
 
G = dict()
Grev = dict()
 
LEADERS = dict()
VERTICES_SORTED_BY_FINISHING_TIMES = []
 
SCCs = dict()
VERTICES_COUNT = 8 # Number of vertices
 
t = 0
s = None
 
def reverse(start, finish):
    i = start
 
    while i >= finish:
        yield i
        i -= 1
 
with open("SCC.txt") as f:
    c = 0
 
    for line in f:
        l = line.rstrip()
        v, u = map(int, l.split(' '))
 
        if v not in G:
            G[v] = []
 
        G[v].append(u)
 
        if u not in G:
            G[u] = []
 
print "[{} sec] graph constructed".format(time.time() - start)
 
### STEP 1
 
EXPLORED = set()
 
for v, arcs in G.iteritems():
    for u in arcs:
        if u not in Grev:
            Grev[u] = []
 
        Grev[u].append(v)
 
    if v not in Grev:
        Grev[v] = []
 
print "[{} sec] reversed graph constructed".format(time.time() - start)
 
### STEP 2
 
EXPLORED = set()
 
def DFS(G, i, step=1):
    global LEADERS, t
 
    EXPLORED.add(i)
 
    if step == 2:
        LEADERS[i] = s
 
    if i not in G:
        return
 
    for j in G[i]:
        if j not in EXPLORED:
            DFS(G, j, step)
 
    if step == 1:
        t += 1
        VERTICES_SORTED_BY_FINISHING_TIMES.append(i)
 
for i in reverse(VERTICES_COUNT, 1):
    if i not in EXPLORED:
        s = i
        DFS(Grev, i)
 
print "[{} sec] vertices sorted by finishing times".format(time.time() - start)
 
### STEP 3
 
EXPLORED = set()
LEADERS = dict()
s = None
 
for i in reversed(VERTICES_SORTED_BY_FINISHING_TIMES):
    if i not in EXPLORED:
        s = i
        DFS(G, i, step=2)
 
print "[{} sec] SCC's revealed".format(time.time() - start)
 
for vertex, leader in LEADERS.iteritems():
    if leader not in SCCs:
        SCCs[leader] = []
 
    SCCs[leader].append(vertex)
 
lengths = []
 
for scc in SCCs.itervalues():
    lengths.append(len(scc))
 
print heapq.nlargest(5, lengths)
print "[{} sec] finished".format(time.time() - start)

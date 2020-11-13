"""
Given N servers and costs of connecting them, minimize the cost 
such that all servers are connected together.


>   Essentially Minimum Spanning Tree

"""
from collections import defaultdict
class Edge():
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    def either(self):
        return self.v
    def other(self, i):
        return self.w if i == self.v else self.v
    def __str__(self):
        return (self.v, self.w, self.weight)
class EdgeWeightGraph():
    def __init__(self, graph):
        
        self.vertices = {}
        self.adj = defaultdict(list)
        self.E, self.V = 0, 0
        
        for e in graph:
            if e[0] not in self.vertices:
                self.vertices[e[0]] = self.V
                self.V += 1
            if e[1] not in self.vertices:
                self.vertices[e[1]] = self.V
                self.V += 1
            
            edge = Edge(self.vertices[e[0]], self.vertices[e[1]], e[2])
            self.E += 1
            self.adj[self.vertices[e[0]]].append(edge) 
            self.adj[self.vertices[e[1]]].append(edge) 
        print(self.adj, self.vertices)
    def edges(self):
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                edges.append(e) if e.other(v) > v else None
    def vName(self, n):
        for k in self.vertices:
            if n == self.vertices[k]:
                return k
    # edge => 'B', 'C', 1
from heapq import * 
from collections import deque
def getMST(graph: EdgeWeightGraph):
    pq = []
    marked = [False for _ in range(graph.V)]
    mst = deque()
    def visit(v):
        marked[v] = True
        for e in graph.adj[v]:
            if (not marked[e.other(v)]):
                heappush(pq, (e.weight, e))
    
    visit(0)
    while pq:
        weight, e = heappop(pq)
        v = e.either() 
        w = e.other(v)
        if marked[v] and marked[w]:
            continue
        mst.append(e)
        if not marked[v]:
            visit(v)
        if not marked[w]:
            visit(w)

    return mst
def getMinCost(N, serverGraph):
    # minimum spanning tree (MST)
    # build an edge weighted 
    graph = EdgeWeightGraph(serverGraph)
    
    mt = getMST(graph)
    res = []
    for e in mt:
        v = e.either()
        w = e.other(v)
        res.append([graph.vName(v), graph.vName(w), e.weight])
    return res
num = 5
connection = [['A','B',1],
	 ['B','C',4],
	 ['B','D',6],
	 ['D','E',5],
	 ['C','E',1]
    ]

t = [['A','B',1],
['B','C',4],
['C','E',1],
['D','E',5]]
print(getMinCost(num, connection))
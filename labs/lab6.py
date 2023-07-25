# Implementation of Dijkstra algorithm

import heapq

class Edge(object):
    
    def __init__(self, weight, startVertex, targetVertex ):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
        
        
class Graph(object):
    
    def __init__(self, graph):
        self.graph = graph
    
    def getAdjacenciesList(self, node):
        adjlist = self.graph[node]
        edgeList = []
        for k,v in adjlist.items():
            edgeList.append(Edge(v, node, k))
        
        return edgeList
        

def dijkstra(graph, start, target):
    g = Graph(graph)
    distances = { node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = []
    heapq.heappush(unvisited, (0, start) )
    previous = { node: None for node in graph}
    
    while unvisited:
        
        actualVertex = heapq.heappop(unvisited)
        if target == actualVertex[1]:
            return distances[target]
        
        for edge in g.getAdjacenciesList(actualVertex[1]):
            u = edge.startVertex
            v = edge.targetVertex
            newDistance = distances[u] + edge.weight
            
            if newDistance < distances[v]:
                previous[v] = u
                distances[v] = newDistance
                heapq.heappush(unvisited, (distances[v], v))
                
    
    
if __name__ == "__main__":
    graph = { 'A': {'B': 2, 'C': 1},'B': {'A': 2, 'C': 2, 'D': 1},'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},'E': {'C': 3, 'D': 1, 'F': 1},'F': {'D': 2, 'E': 1, 'G': 3},'G': {'F': 3}}
    
    dis = dijkstra(graph, 'A', 'F')
    print("Distance from A to F : " + str(dis))
    
    dis = dijkstra(graph, 'B', 'G')
    print("Distance from B to G : " + str(dis))
    
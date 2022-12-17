from queue import PriorityQueue
from model.graph import Graph

def dijkstra(graph: Graph, start_vertex):
    G = DGraph(graph.NumberOfVertices)
    for edge in graph.Edges:
        G.add_edge(edge.X, edge.Y, edge.Weight)

    D = {v:float('inf') for v in range(G.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        G.visited.append(current_vertex)

        for neighbor in range(G.v):
            if G.edges[current_vertex][neighbor] != -1:
                distance = G.edges[current_vertex][neighbor]
                if neighbor not in G.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

class DGraph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
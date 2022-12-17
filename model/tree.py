from function.dijkstra import dijkstra
from model.edge import Edge
from model.graph import Graph

class Tree:

    def __init__(self, numberOfVertices: int):
        self.NumberOfVertices = numberOfVertices
        self.Edges = []

    def add_edge(self, edge: Edge):
        self.Edges.append(edge)
    
    def remove_edge(self, edge: Edge):
        for e in self.Edges:
            if edge.are_edge_equal(e):
                self.Edges.remove(edge)
                break
    
    def get_vertices_with_odd_degree(self):
        collector = [0 for x in range(self.NumberOfVertices)]
        result = []

        for edge in self.Edges:
            collector[edge.X] += 1
            collector[edge.Y] += 1

        index = 0
        for vertex in collector:
            if vertex % 2 != 0:
                result.append(index)
            index += 1

        return result

    def get_subgraph_with_vertices_is_odd(self, graph):
        G = Graph(self.NumberOfVertices)
        vertices = self.get_vertices_with_odd_degree()
        
        self.collect_all_possible_new_edges(G, graph, vertices)
        
        for edge in G.Edges:
            values = dijkstra(G, edge.X)
            edge.Weight = values[edge.Y]
        return G.Edges

    def collect_all_possible_new_edges(self, G, old_graph, vertices):
        for vertex1 in vertices:
            for vertex2 in vertices:
                if vertex1 != vertex2:
                    edge = Edge(vertex1, vertex2, -1)
                    edge.Weight = self.get_edge_weight_from_graph(old_graph, edge)
                    if not G.is_edge_in_graph(edge):
                        G.add_edge(edge)

    def get_edge_weight_from_graph(self, G, edge):
        for e in G.Edges:
            if e.are_edge_equal(edge):
                return e.Weight
        return -1
    
    def add_edges_from_graph(self, graph):
        for edge in graph.Edges:
            self.add_edge(edge)



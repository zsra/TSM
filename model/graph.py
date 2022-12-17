from model.edge import Edge

class Graph:

    def __init__(self, numberOfVertices: int):
        self.Edges = []
        self.NumberOfVertices = numberOfVertices

    def add_edge(self, edge: Edge):
        self.Edges.append(edge)

    def is_edge_in_graph(self, edge):
        isContains = False
        for e in self.Edges:
            if e.are_edge_equal(edge):
                isContains = True
                break
        return isContains

    def create_graph_from_edges(self, raw_edges):
        result = Graph(self.NumberOfVertices)
        for edge in self.Edges:
            for re in raw_edges:
                new_edge = Edge(re[0], re[1], 0)
                if edge.are_edge_equal(new_edge):
                    result.add_edge(edge)
        return result

    def get_vertices_freq_order(self):
        vertices_collector = [0 for x in range(self.NumberOfVertices)]
        dict = {}
        counter = 0

        for edge in self.Edges:
            vertices_collector[edge.X] += edge.Weight
            vertices_collector[edge.Y] += edge.Weight
        
        for value in vertices_collector:
            dict[counter] = value
            counter += 1

        return list({k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}.keys())

    def order_edges(self):
        collector = Graph(self.NumberOfVertices)
        visited = Graph(self.NumberOfVertices)
        
        for vertex in self.get_vertices_freq_order():
            for edge in self.Edges:
                if (not visited.is_edge_in_graph(edge)) and (edge.X == vertex):
                    collector.add_edge(Edge(vertex, edge.Y, edge.Weight))
                    visited.add_edge(edge)
                if (not visited.is_edge_in_graph(edge)) and (edge.Y == vertex):
                    collector.add_edge(Edge(vertex, edge.X, edge.Weight))
                    visited.add_edge(edge)

        return sorted(collector.Edges) 
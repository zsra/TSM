import unittest
from function.kruskal import kruskal
from function.matching import min_weight_matching
from model.graph import Graph
from model.edge import Edge
from function.eulerian import find_eulerian_tour

class EulerianTests(unittest.TestCase):

    def test_exec_eulerian(self):
        graph = Graph(5)
        graph.add_edge(Edge(0, 1, 1))
        graph.add_edge(Edge(0, 2, 1))
        graph.add_edge(Edge(0, 3, 1))
        graph.add_edge(Edge(0, 4, 2))
        graph.add_edge(Edge(1, 2, 1))
        graph.add_edge(Edge(1, 3, 2))
        graph.add_edge(Edge(1, 4, 1))
        graph.add_edge(Edge(2, 3, 1))
        graph.add_edge(Edge(2, 4, 1))
        graph.add_edge(Edge(3, 4, 1))

        k = kruskal(graph)
        o = k.get_subgraph_with_vertices_is_odd(graph)
        m = min_weight_matching(o)
        k.add_edges_from_graph(graph.create_graph_from_edges(m))

        result = find_eulerian_tour(k)
        
        self.assertIsNotNone(result)
        self.assertEqual(result, [Edge(2, 0, 1), Edge(0, 3, 1), Edge(3, 2, 1), Edge(2, 1, 1), Edge(1, 4, 1), Edge(4, 2, 1)])

    if __name__ == '__main__':
        unittest.main()
import unittest
from model.edge import Edge
from model.graph import Graph
from function.kruskal import kruskal
from function.matching import min_weight_matching

class MatchingTests(unittest.TestCase):
    
    def test_min_weight_matching(self):
        graph = Graph(6)
        graph.add_edge(Edge(0, 1, 7))
        graph.add_edge(Edge(0, 2, 8))
        graph.add_edge(Edge(1, 2, 3))
        graph.add_edge(Edge(1, 4, 6))
        graph.add_edge(Edge(2, 3, 3))
        graph.add_edge(Edge(3, 4, 4))
        graph.add_edge(Edge(4, 4, 2))
        graph.add_edge(Edge(3, 5, 2))
        graph.add_edge(Edge(4, 5, 2))

        k = kruskal(graph)
        o = k.get_subgraph_with_vertices_is_odd(graph)
        m = min_weight_matching(o)
        self.assertEqual(m, {(0, 4)})
        
    def test_min_weight_matching2(self):
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
        
        self.assertEqual(m, {(4, 1), (3, 0)})

    if __name__ == '__main__':
        unittest.main()    
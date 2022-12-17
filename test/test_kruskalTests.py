import unittest
from model.graph import Graph
from model.edge import Edge
from function.kruskal import kruskal

class KruskalTests(unittest.TestCase):

    def test_exec_kruskal(self):
        graph = Graph(6)
        graph.add_edge(Edge(0, 1, 7))
        graph.add_edge(Edge(0, 2, 8))
        graph.add_edge(Edge(1, 2, 3))
        graph.add_edge(Edge(1, 4, 6))
        graph.add_edge(Edge(2, 3, 3))
        graph.add_edge(Edge(2, 4, 4))
        graph.add_edge(Edge(3, 4, 2))
        graph.add_edge(Edge(3, 5, 2))
        graph.add_edge(Edge(4, 5, 2))

        result = kruskal(graph)

        self.assertIsNotNone(result)
        self.assertEqual(len(result.Edges), 5)
        self.assertEqual(result.Edges, [Edge(3, 4, 2), Edge(3, 5, 2), Edge(1, 2, 3), Edge(2, 3, 3), Edge(0, 1, 7)])

    if __name__ == '__main__':
        unittest.main()
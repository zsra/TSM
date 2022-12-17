import unittest
from model.graph import Graph
from model.edge import Edge
from function.dijkstra import dijkstra

class DijkstraTests(unittest.TestCase):

    def test_exec_dijkstra(self):
        graph = Graph(9)
        graph.add_edge(Edge(0, 1, 4))
        graph.add_edge(Edge(0, 6, 7))
        graph.add_edge(Edge(1, 6, 11))
        graph.add_edge(Edge(1, 7, 20))
        graph.add_edge(Edge(1, 2, 9))
        graph.add_edge(Edge(2, 3, 6))
        graph.add_edge(Edge(2, 4, 2))
        graph.add_edge(Edge(3, 4, 10))
        graph.add_edge(Edge(3, 5, 5))
        graph.add_edge(Edge(4, 5, 15))
        graph.add_edge(Edge(4, 7, 1))
        graph.add_edge(Edge(4, 8, 5))
        graph.add_edge(Edge(5, 8, 12))
        graph.add_edge(Edge(6, 7, 1))
        graph.add_edge(Edge(7, 8, 3))

        result = dijkstra(graph, 0)

        self.assertIsNotNone(result)
        self.assertEqual(result, {0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11})

    if __name__ == '__main__':
        unittest.main()
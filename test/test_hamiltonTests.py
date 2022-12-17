import unittest
from function.hamilton import find_hamilton_path
from function.kruskal import kruskal
from function.matching import min_weight_matching
from model.graph import Graph
from model.edge import Edge
from function.eulerian import find_eulerian_tour

class hamiltonTests(unittest.TestCase):

    def test_exec_hamilton(self):
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

        eulerian = find_eulerian_tour(k)
        eulerian_tour = find_hamilton_path(eulerian, eulerian[0].X)

        self.assertIsNotNone(eulerian_tour)
        self.assertEqual(eulerian_tour, [0, 2, 1, 4, 3, 0])

    if __name__ == '__main__':
        unittest.main()
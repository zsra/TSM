import unittest
from function.kruskal import kruskal
from function.matching import min_weight_matching
from model.graph import Graph
from model.edge import Edge
from model.tree import Tree
from model.disjointSet import DisjointSet

class ModelTests(unittest.TestCase):
    
    def test_edge_creation(self):
        edge = Edge(1, 2, 5)
        
        self.assertIsNotNone(edge)
        self.assertEqual(edge.X, 1)
        self.assertEqual(edge.Y, 2)
        self.assertEqual(edge.Weight, 5)

    def test_graph_creation(self):
        graph = Graph(3)
        graph.add_edge(Edge(0, 1, 5))
        graph.add_edge(Edge(1, 2, 5))

        self.assertIsNotNone(graph)
        self.assertEqual(len(graph.Edges), 2)

    def test_disjointset_creation(self):
        disjointset = DisjointSet(5)

        self.assertIsNotNone(disjointset)
        self.assertIsNotNone(disjointset.parent)
        self.assertEqual(disjointset.rank, [0, 0, 0, 0, 0])

    def test_disjointset_find(self):
        disjointset = DisjointSet(5)

        self.assertEqual(disjointset.find(4), 4)

    def test_disjointset_union(self):
        disjointset = DisjointSet(5)

        disjointset.union(2, 3)

        self.assertEqual(disjointset.parent, [0, 1, 2, 2, 4])
        self.assertEqual(disjointset.rank, [0, 0, 1, 0, 0])

    def test_tree_creation(self):
        treeCreation = Tree(3)
        treeCreation.add_edge(Edge(1, 2, 5))
        treeCreation.add_edge(Edge(2, 3, 5))

        self.assertIsNotNone(treeCreation)
        self.assertEqual(len(treeCreation.Edges), 2)

    def test_tree_odd_vertices(self):
        tree = Tree(6)
        tree.add_edge(Edge(0, 1, 7))
        tree.add_edge(Edge(1, 2, 3))
        tree.add_edge(Edge(2, 3, 3))
        tree.add_edge(Edge(3, 4, 2))
        tree.add_edge(Edge(3, 5, 2))

        result = tree.get_vertices_with_odd_degree()

        self.assertIsNotNone(result)
        self.assertEqual(result, [0, 3, 4, 5])

    def test_add_edges_from_tree(self):
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

        self.assertIsNotNone(k)
        self.assertEqual(k.Edges, [Edge(2, 0, 1), Edge(2, 1, 1), Edge(2, 3, 1), Edge(2, 4, 1), Edge(0, 3, 1), Edge(1, 4, 1)])

if __name__ == '__main__':
    unittest.main()
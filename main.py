from function.christofides import christofides
from model.edge import Edge
from model.graph import Graph

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

result = christofides(graph)

print("path: ", result)

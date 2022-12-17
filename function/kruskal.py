from model.edge import Edge
from model.graph import Graph
from model.disjointSet import DisjointSet
from model.tree import Tree

def kruskal(graph: Graph) -> Tree:
    disjointset = DisjointSet(graph.NumberOfVertices)
    sortedEdges = graph.order_edges()
    edgeCounter = 0
    loopCounter = 0
    tree = Tree(graph.NumberOfVertices)
    
    while edgeCounter < graph.NumberOfVertices - 1:
        edge = sortedEdges[loopCounter]
        sv = disjointset.find(edge.X)
        dv = disjointset.find(edge.Y)

        if(sv != dv):
            tree.add_edge(Edge(edge.X, edge.Y, edge.Weight))
            disjointset.union(sv, dv)
            edgeCounter += 1

        loopCounter += 1
    
    return tree   
    
    

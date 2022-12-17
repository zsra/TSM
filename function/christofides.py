from model.graph import Graph
from function.hamilton import find_hamilton_path
from function.kruskal import kruskal
from function.matching import min_weight_matching
from function.eulerian import find_eulerian_tour

def christofides(graph: Graph):
    k = kruskal(graph)
    o = k.get_subgraph_with_vertices_is_odd(graph)
    m = min_weight_matching(o)
    k.add_edges_from_graph(graph.create_graph_from_edges(m))

    eulerian = find_eulerian_tour(k)
    eulerian_tour = find_hamilton_path(eulerian, eulerian[0].X)

    return eulerian_tour
import networkx as nx

def min_weight_matching(input_edges):
    edges =[]
    for edge in input_edges:
        edges.append((edge.X, edge.Y, edge.Weight))

    nxG = nx.Graph()
    nxG.add_weighted_edges_from(edges)
    return nx.min_weight_matching(nxG)


        
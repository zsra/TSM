from model.edge import Edge
from model.tree import Tree


def find_eulerian_tour(tree: Tree):
    unvisited = tree.Edges
    start_edge = tree.Edges[0]
    result = []

    result.append(start_edge)
    remove_edge_from_list(unvisited, start_edge)

    visitor = start_edge.Y
    while len(unvisited) > 0:
        for edge in unvisited:
            if edge.X == visitor and is_edge_in_list(unvisited, edge):
                result.append(Edge(visitor, edge.Y, edge.Weight))
                remove_edge_from_list(unvisited, edge)
                visitor = edge.Y
                break
            elif edge.Y == visitor and is_edge_in_list(unvisited, edge):
                result.append(Edge(visitor, edge.X, edge.Weight))
                remove_edge_from_list(unvisited, edge)
                visitor = edge.X
                break
    
    return result

def is_edge_in_list(list, edge):
    for e in list:
        if edge.are_edge_equal(e):
            return True
    return False

def remove_edge_from_list(list, edge):
    index = 0
    for e in list:
        if edge.are_edge_equal(e):
            del list[index]
        index += 1

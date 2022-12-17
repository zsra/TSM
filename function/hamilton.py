from model.edge import Edge


def find_hamilton_path(edges, start_vertex):
    neighbours = {}
    for edge in edges:
        if edge.X not in neighbours:
            neighbours[edge.X] = []

        if edge.Y not in neighbours:
            neighbours[edge.Y] = []

        neighbours[edge.X].append(edge.Y)
        neighbours[edge.Y].append(edge.X)

    start_vertex = edges[0].X
    EP = [neighbours[start_vertex][0]]

    while len(edges) > 0:
        for i, v in enumerate(EP):
            if len(neighbours[v]) > 0:
                break

        while len(neighbours[v]) > 0:
            w = neighbours[v][0]

            remove_edge_from_list(edges, Edge(v, w, get_weight_by_vertex(edges, v, w)))

            del neighbours[v][(neighbours[v].index(w))]
            del neighbours[w][(neighbours[w].index(v))]

            i += 1
            EP.insert(i, w)

            v = w

    current = EP[0]
    path = [current]
    visited = [False] * len(EP)
    visited[EP[0]] = True
    length = 0

    for v in EP:
        if not visited[v]:
            path.append(v)
            visited[v] = True

            current = v

    path.append(EP[0])

    return path

def remove_edge_from_list(list, edge):
    index = 0
    for e in list:
        if edge.are_edge_equal(e):
            del list[index]
        index += 1

def get_weight_by_vertex(list, x, w):
    for e in list:
        if (e.X == x and e.Y == w) or (e.X == x and e.Y == w):
            return e.Weight
    return 1
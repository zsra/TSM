class Edge:
    
    def __init__(self, X, Y, weight: float):
        self.X = X
        self.Y = Y
        self.Weight = weight

    def __eq__(self, other):
        return self.is_X_eq(other) or self.is_Y_eq(other) or self.is_weights_eq(other)

    def __lt__(self, other):
        return self.Weight < other.Weight

    def __repr__(self):
        return "(" + str(self.X) + ", " + str(self.Y) + ", " + str(self.Weight) + ")"

    def is_X_eq(self, other):
        return self.X == other.X

    def is_Y_eq(self, other):
        return self.Y == other.Y

    def is_weights_eq(self, other):
        return self.Weight == other.Weight

    def are_edge_equal(self, edge):
        return (edge.X == self.X and edge.Y == self.Y) \
                            or (edge.X == self.Y and edge.Y == self.X)
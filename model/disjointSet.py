class DisjointSet:
    
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0 for x in range(size)]
        self.size = size
    
    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        else:
            return x
    
    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        
        if x != y:
            
            if self.rank[x] < self.rank[y]:
                temp = x
                x = y
                y = temp
            
            self.parent[y] = x

            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

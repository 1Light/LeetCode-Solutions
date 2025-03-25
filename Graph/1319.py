# 1319. Number of Operations to Make Network Connected (Mode: Medium)

class Solution(object):
    
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        # len(connection) = number of wire
        # at least n - 1 wire is needed to  connect all
        if len(connections) < n - 1:
            return -1
        
        # Union-Find (Disjoint Set Union) implementation

        # list of computer groups
        # same groups will have same value - [0, 0, 2, 3] - 
        parent = list(range(n))

        # depth of the tree formed by union
        rank = [0] * n
        
        # path compression to make system faster
        def find(x):
            if parent[x] != x: # - if not equal, it means it joined another group
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # Union by rank to optimize
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
            
            # if rootX == rootY, then they are in the same group
        
        # Process each connection and union the nodes
        for a, b in connections:
            union(a, b)
        
        # Count the number of computer groups
        groups = sum(1 for i in range(n) if find(i) == i)
        
        # We need at least `groups - 1` cables to connect all groups
        return groups - 1
        
        
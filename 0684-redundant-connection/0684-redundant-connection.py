class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False # this means that cycle is detected
            
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True

        for edge in edges:
            parent[edge[0]] = edge[0]
            parent[edge[1]] = edge[1]
            rank[edge[0]] = 0
            rank[edge[1]] = 0

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        return []

class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        import heapq

        r,c = len(grid), len(grid[0])
        visited = []        
        for i in range(r):
            row = [0]*c
            visited.append(row)
        vol = 0
        PQ = [] # (val, (i,j))

        for i in range(r):
            for j in range(c):
                # if boundary, add those cells to PQ and mark visited
                if i == 0 or j == 0 or i == r-1 or j == c - 1:
                    heapq.heappush(PQ, ( grid[i][j], (i , j) ))
                    visited[i][j] = 1
        
        print(PQ)
        # heapq.heapify(PQ)
        minBoundaryHeight = 0

        while len(PQ) != 0:
            currHt, coordinates = heapq.heappop(PQ)
            minBoundaryHeight = max(minBoundaryHeight, currHt)
            i,j = coordinates

            # visit the neighbors of the (i,j): up, down, right, left
            dr = [0,0,-1, 1]
            dc = [1,-1,0,0]
            for idx in range(4):
                nR = i + dr[idx]
                nC = j + dc[idx]
                # check that (neighbor_i, neighbor_j) is within grid
                if 0 <= nR < r and 0 <= nC < c and visited[nR][nC] == 0:
                    # push that neight to PQ
                    heapq.heappush(PQ, (grid[nR][nC], (nR, nC)))
                    # mark that neighbor as visited
                    visited[nR][nC] = 1
                    # check if neighbor cell can be filled with water
                    ## if grid[nR][nC] < minBoundaryHeight => 
                    if grid[nR][nC] < minBoundaryHeight: 
                        vol += minBoundaryHeight - grid[nR][nC]
    
        return vol
        
        
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        # Brute Force
        mat = []
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(0)
            mat.append(arr)
        
        for indx in indices:
            r,c = indx
            for col in range(n):
                mat[r][col] += 1
            for row in range(m):
                mat[row][c] += 1
            
        oddCount = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 == 1:
                    oddCount += 1

        return oddCount




        
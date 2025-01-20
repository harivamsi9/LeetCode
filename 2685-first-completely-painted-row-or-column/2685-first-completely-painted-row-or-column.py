from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_counts = [n] * m  # Each row has 'n' elements
        col_counts = [m] * n  # Each column has 'm' elements
        arrDict = {}  # Map from element in mat to its (row, column)

        # Create a mapping of matrix values to their positions
        for i in range(m):
            for j in range(n):
                arrDict[mat[i][j]] = (i, j)

        # Process elements in the order they appear in arr
        for idx in range(len(arr)):
            i, j = arrDict[arr[idx]]  # Get the row and column of the current element

            # Decrement the counts for the corresponding row and column
            row_counts[i] -= 1
            col_counts[j] -= 1

            # Check if any row or column is completely zero
            if row_counts[i] == 0 or col_counts[j] == 0:
                return idx

        return -1  # Return -1 if no row or column is fully completed

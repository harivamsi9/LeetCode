class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_counts = [n]*m
        col_counts = [m]*n
        arrDict = dict()
        # print(row_counts, col_counts)
        for i in range(m):
            for j in range(n):
                arrDict[mat[i][j]] = (i,j)
        # print(arrDict)
        for idx in range(len(arr)):
            i,j = arrDict[arr[idx]] # (i,j)
            # print(f"{i}, {j}, {arr[idx]}")

            col_counts[j] -= 1
            row_counts[i] -= 1
            # print(row_counts, col_counts)
            if col_counts[j] ==0 or row_counts[i] == 0:
            # if 0 in col_counts or 0 in row_counts:
                # print(arr[idx])
                return idx

        return idx

        
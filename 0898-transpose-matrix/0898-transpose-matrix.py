class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Ezample:
        A = [
            (0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2)
        ]

        A^T = [
            (0,0), (0,1), (0,2),
            (0,1), (1,1), (1,2),
            (0,2), (1,2), (2,2)
        ]
        Example 2: [
            [1,2,3],
            [4,5,6]
        ]
        Ans:
        [
            [1,4],
            [2,5],
            [3,6]
        ]

        """
        # print(matrix[2])
        ans = []
        for j in range(len(matrix[0])):
            arr = []
            for i in range(len(matrix)):
                arr.append(0)
            ans.append(arr)
        print(ans)
        col = 0
        for i in range(len(matrix)): 
            row = 0
            Org_row = matrix[i]
            # print(Org_row)
            for k in Org_row:
                print(row,col)
                ans[row][col] = k
                row += 1
            col += 1
        return ans
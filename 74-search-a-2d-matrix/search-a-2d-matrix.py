class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j ==0:
                    first_col.append(matrix[i][j])
        
        start= 0
        end= len(first_col) -1
        while start <= end:
            mid = start + (end - start) // 2
            if target > first_col[mid]:
                start = mid + 1
            elif target < first_col[mid]:
                end = mid - 1
            else:
                return True
        
        possible_row = end

        row = []
        for i in range(len(matrix)):
            # for j in range(len(matrix[0])):
            if i == end:
                row.extend(matrix[i])

        start= 0
        end= len(row) - 1
        print(row)
        while start <= end:
            mid = start + (end - start) // 2
            if target > row[mid]:
                start = mid + 1
            elif target < row[mid]:
                end = mid - 1
            else:
                return True
        return False


        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = []
        
        top = 0
        bot = len(matrix) -1

        while top <= bot:
            mid = top + (bot - top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        possible_row = top + (bot - top) // 2
        
        # perform the BS on this row in the 2d Matrix
        start= 0
        end= len(matrix[0]) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if target > matrix[possible_row][mid]:
                start = mid + 1
            elif target < matrix[possible_row][mid]:
                end = mid - 1
            else:
                return True
        return False


        
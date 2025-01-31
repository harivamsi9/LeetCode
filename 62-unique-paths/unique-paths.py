class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        dp = []

        for r in range(ROWS):
            row = [0]*COLS
            dp.append(row)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dp[r][c] = 1

        for i in range(ROWS):
            for j in range(COLS):
                if not(i == 0 or j == 0):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
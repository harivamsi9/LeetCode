from typing import List
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # Initialize DP table: dp[i][j][k] is the max profit at (i, j) with k neutralizations left
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base case: Starting point
        for k in range(3):  # All possible neutralization counts
            dp[0][0][k] = max(0, coins[0][0]) if coins[0][0] < 0 and k > 0 else coins[0][0]
        
        # Fill DP table
        for i in range(m):
            for j in range(n):
                for k in range(3):  # Remaining neutralizations
                    if i > 0:
                        # Coming from above
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                        if k > 0 and coins[i][j] < 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                    if j > 0:
                        # Coming from the left
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
                        if k > 0 and coins[i][j] < 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        
        # Return the maximum profit at the bottom-right corner
        return max(dp[m-1][n-1])


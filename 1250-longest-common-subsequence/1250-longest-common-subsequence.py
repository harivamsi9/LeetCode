class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = '#' + text1
        text2 = '#' + text2
        
        dp = []
        for i in range(len(text1)):
            ls = []
            for j in range(len(text2)):
                ls.append(0)
            dp.append(ls)
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                # empty strings => dp[i][j] = 0
                if i == 0 or j == 0:
                # if text1[i] == '#' or text2[j]=='#':
                    dp[i][j] = 0
                # 1 + dp[i-1][j-1] => Matching Chars
                elif text1[i] == text2[j]:
                    dp[i][j] =  1 + dp[i-1][j-1]
                # Mis-Match Chars => MAX(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
            
            
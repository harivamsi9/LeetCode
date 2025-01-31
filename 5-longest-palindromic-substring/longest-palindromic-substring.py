class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = "cbbd"
        maxCount = float('-inf')
        ans1 = ""

        for i in range(len(s)): # "cbbd"
            count1 = 0
            # odd length
            j, k = i, i
            while 0 <= j < len(s) and 0 <= k < len(s) and s[j] == s[k]:
                count1 += 1
                j -= 1
                k += 1
            
            if count1 > maxCount:
                maxCount = count1  # This is fine, no need for max(maxCount, count1)
                ans1 = s[j+1:k]

        maxCount2 = float('-inf')
        ans2 = ""
        for i in range(len(s)):
            count2 = 0
            # even length
            j, k = i, i + 1
            while 0 <= j < len(s) and 0 <= k < len(s) and s[j] == s[k]:
                count2 += 1
                j -= 1
                k += 1
            
            if count2 > maxCount2:
                maxCount2 = count2  # Same here, just use count2
                ans2 = s[j+1:k]
        print(ans1, ans2)

        return ans1 if len(ans1) > len(ans2) else ans2
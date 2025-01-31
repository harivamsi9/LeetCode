class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_count = 0
        ans = ''
        for i in range(len(s)):
            j,k = i,i
            count = 0
            while j >=0 and k <= len(s)-1 and s[j] == s[k]:
                count += 1
                j -= 1
                k += 1
            
            if count > max_count: 
                ans = s[j+1:k]
                max_count = max(count, max_count)

        ans2 = ''
        max_count2 = 0
        for i in range(len(s)):
            j,k = i,i+1
            count = 0
            while j >=0 and k <= len(s)-1 and s[j] == s[k]:
                count += 1
                j -= 1
                k += 1
            
            if count > max_count2: 
                ans2 = s[j+1:k]
                max_count2 = max(count, max_count2)
            
        print(ans, ans2)

        return ans if len(ans) > len(ans2) else ans2
            
        
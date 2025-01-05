class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ## Difference Array Approach
        ## Time Complexity - O(N)
        ## Space Complexity - O(N)
        
        diffArr = [0]*len(s)

        for q in shifts:
            l,r,x = q
            if x == 0:
                x = -1
            else:
                x = 1
        
            diffArr[l] += x
            if r+1 < len(s):
                diffArr[r+1] -= x

        ps = [0]*len(s)
        ps[0] = diffArr[0]

        ans = ''
        for i in range(0,len(s)):
            if i > 0:
                ps[i] += diffArr[i] + ps[i-1]
            newChar_ord = ord('a') + ((ord(s[i]) - ord('a') + ps[i]) % 26)
            newChar = chr(newChar_ord)
            ans += newChar
        return ans



            
        
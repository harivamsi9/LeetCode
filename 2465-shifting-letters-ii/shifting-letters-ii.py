class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
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
        for i in range(1,len(s)):
            ps[i] += diffArr[i] + ps[i-1]
        print(diffArr)
        print(ps)
        ans = ''
        for i in range(len(s)):
            newChar_ord = ord('a') + ((ord(s[i]) - ord('a') + ps[i]) % 26)
            newChar = chr(newChar_ord)
            ans += newChar
        return ans



            
        
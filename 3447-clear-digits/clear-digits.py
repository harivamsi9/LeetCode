class Solution:
    def clearDigits(self, s: str) -> str:
        dc = 0
        cc = 0 
        j = len(s) - 1
        ans = []

        while j >= 0:
            if s[j] in "1234567890":
                dc += 1
                j -= 1
            else:
                if dc > 0:
                    dc -= 1
                    j -= 1
                else:
                    ans.append(s[j])
                    j-=1

        # print(ans)
        res = "".join(ans[::-1])
        return res


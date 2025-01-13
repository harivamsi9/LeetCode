class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for k,v in c.items():
            if v < 3: ans += v
            else:
                while v >2: v -= 2
                ans += v

        return ans

        
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        if len(s) == k: return True
        c = Counter(s)
        count = 0
        for key,val in c.items():
            if val%2 == 1:
                count += 1
            
            if count > k:
                return False
        return True


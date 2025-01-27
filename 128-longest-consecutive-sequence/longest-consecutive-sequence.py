class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup = set()
        for n in nums:
            lookup.add(n)
        c_max = 0
        for n in lookup:
            if (n-1) in lookup:
                continue
            else:
                c = 0 
                while n in lookup:
                    c += 1
                    n += 1
                    c_max = max(c, c_max)
        return c_max
        
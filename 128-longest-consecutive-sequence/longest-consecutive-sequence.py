class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        max_ = 0
        for i in set_:
            if i-1 not in set_:  
                c = 0
                while i+c in set_:
                    c += 1
                max_ = max(c,max_)
        return max_
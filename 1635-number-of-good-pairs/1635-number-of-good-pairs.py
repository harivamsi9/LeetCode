class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ## Brute Force
        count = 0
        for j in range(1,len(nums)):
            for i in range(j):
                if nums[i] == nums[j]:
                    count += 1
        return count
                    
        
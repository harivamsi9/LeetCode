class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-2):
            if nums[i] == nums[i+1] or nums[i] == nums[i+2]:
                return nums[i]
            if nums[i+1] == nums[i+2]: return nums[i+1]
            if i+2 == len(nums)-1 and nums[-1] == nums[0]:
                return nums[0]
                
        return -1
            
        
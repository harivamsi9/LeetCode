class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = 0
        for i in range(len(nums)):
            rs += nums[i]
            nums[i] = rs

        return nums
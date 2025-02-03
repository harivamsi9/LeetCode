class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLen_incre = 1
        if len(nums) == 1: return 1
        if len(nums) == 0: return 0

        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                maxLen_incre = max(maxLen_incre, dp[i])
            else:
                dp[i] = 1
        
        maxLen_desc = 1
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                dp[i] = dp[i-1] + 1

                maxLen_desc  = max(maxLen_desc, dp[i])
            else:
                dp[i] = 1
        return max(maxLen_desc, maxLen_incre)
        
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        dp = [float('-inf')]*len(nums)
        minProd = 1
        maxProd = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                dp[i] = 0
                minProd = 1
                maxProd = 1
                continue
            
            prev_maxProd = maxProd
            prev_minProd = minProd

            maxProd = max(maxProd*nums[i], minProd*nums[i], nums[i])
            minProd = min(prev_maxProd*nums[i], minProd*nums[i], nums[i])

            dp[i] = max(maxProd, minProd)
        return max(dp)



        
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # prefixSum, suffixSum

        prefixSum, suffixSum = [0]*len(nums), [0]*len(nums)
        prefixSum[0] = nums[0]
        suffixSum[-1] = nums[-1]

        counts = 0

        for i in range(len(nums)-1-1,-1,-1):
            suffixSum[i] += nums[i] + suffixSum[i+1]

        for i in range(1, len(nums)):
            prefixSum[i] += nums[i] + prefixSum[i-1]

        for i in range(0, len(nums)-1):
            if prefixSum[i] >= suffixSum[i+1]: counts += 1
        return counts


        

        

        
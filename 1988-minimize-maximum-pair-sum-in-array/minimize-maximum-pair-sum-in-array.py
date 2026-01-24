class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # in-place sort O(n.logn)
        nums.sort()
        ans = float('-inf')
        i = 0
        j = len(nums) - 1
        while i < j:
            if ans < nums[i] + nums[j]:
                ans = nums[i] + nums[j]
            i+=1
            j-=1
        return ans



        
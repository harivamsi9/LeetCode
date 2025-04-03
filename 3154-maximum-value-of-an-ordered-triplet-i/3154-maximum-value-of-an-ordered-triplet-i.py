class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxi = 0
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1, len(nums)):
                    ans = (nums[i] - nums[j]) * nums[k]
                    maxi = max(ans, maxi)

        return maxi

        
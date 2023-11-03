class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # brute Force TC: O(N^2) SC: O(N)
        ans = []
        for i in range(0,len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans

                    
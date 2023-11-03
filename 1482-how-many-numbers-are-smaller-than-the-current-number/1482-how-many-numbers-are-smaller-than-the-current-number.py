class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # ## brute Force TC: O(N^2) SC: O(N)
        # ans = []
        # for i in range(0,len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if i != j and nums[j] < nums[i]:
        #             count += 1
        #     ans.append(count)
        # return ans

        ## Approach 1: Time Optimization
        # sort the array
        ans = nums.copy()
        # ans = list(set(ans))
        ans.sort()
        dict_1 = {}
        for j in range(0,len(ans)):
            if ans[j] not in dict_1:
                dict_1[ans[j]] = j 
        for i in range(len(nums)):
            nums[i] = dict_1[nums[i]]
        return nums




                    
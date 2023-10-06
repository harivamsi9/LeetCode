class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictSum = {}

        # [2, 7, 11, 15] , 9
        # # 9 - nums[i]
        # [7 -> 0, 2 -> 1, -2 -> 2, -4 -> 3]

        # [3,2,4], 6
        ## 6 - nums[i]
        # 
        for i in range(len(nums)):
            dictSum[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in dictSum.keys() and i != dictSum[nums[i]]:
                ans = [i]
                ans.append(dictSum[nums[i]])
                return ans
            
        
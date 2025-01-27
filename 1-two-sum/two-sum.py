class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vis = {} # val -> index
        for i in range(len(nums)):
            if nums[i] in vis:
                return [i, vis[nums[i]]]
            diff = target - nums[i]
            vis[diff] = i
        return [-1,-1]
            





        # brute force
        ## TC - O(); SC - O()
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return [-1,-1]

        
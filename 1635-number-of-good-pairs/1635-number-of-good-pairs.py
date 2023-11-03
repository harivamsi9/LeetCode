class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ## Brute Force TC: O(N^2) SC: O(1)
        # count = 0
        # for j in range(1,len(nums)):
        #     for i in range(j):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count

        # # optimized TC: O(2N) SC: O(N)
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        count = 0
        for i in counter.keys():
            n = counter[i]
            count += n*(n-1)//2
        return count




                    
        
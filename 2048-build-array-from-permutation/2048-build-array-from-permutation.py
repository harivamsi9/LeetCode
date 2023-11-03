class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # brute force
        # ans = []
        # for i in range(len(nums)):
        #     elem = nums[nums[i]]
        #     ans.append(elem)
        # return ans

        """
        ###### Space optimized solution
        **Intuition: **

        We need to find a way to store both the nums[i] orginal value as well as the nums[nums[i]] value. 
        Since manipulating the nums in-place will distort the orginal values and we may not be able to use them again for later to modify other indexes.
        Since 1 <= nums.length <= 1000 which means that there are more empty bits in the INTEGER for it hold the extra information.
        We use this constraint as a HACK to store both orginal and modified value of an index as a Single Integer. We call this as the meta information.

        **Idea:**
        meta = num1 + num2 * SCALING_FACTOR

        Let a = nums[i] and b = nums[nums[i]] and c = SCALING_FACTOR
        SCALING_FACTOR >= 1000 or we can also say that SCALING_FACTOR = n+1; n = len(nums)
        therefore,
        meta = a + b * c
        we further re-write b = nums[nums[i] % c] 
        Also, 
        to retrieve a (i.e nums[i]), we can simply do meta % c ; similarly,
        to retrieve b (i.e nums[nums[i]]), we can do meta // c;

        **Solution:**
        We first modify the nums in-place with the value meta, then re-iterative nums again and modify nums in-place with meta/c to get the final modified nums with updated values.

        """
        c = len(nums)
        for i in range(len(nums)):
            a = nums[i]
            b = nums[a] % c
            meta = a + c * b
            nums[i] = meta

        for i in range(len(nums)):
            nums[i] = nums[i] // c
        return nums


            

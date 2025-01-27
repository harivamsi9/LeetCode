class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        base = 1
        ps = [1]*len(nums)

        for i in range(1,len(nums)):
            ps[i] = nums[i-1] * ps[i-1]
        
        ss = [1] * len(nums)
        for i in range(len(nums)-1 -1, -1 ,-1):
            ss[i] = nums[i+1] * ss[i+1]
        
        prod = [1] * len(nums)
        print(ps)
        print(ss)
        for i in range(len(nums)):
            prod[i] = ss[i]*ps[i]

        return prod

        
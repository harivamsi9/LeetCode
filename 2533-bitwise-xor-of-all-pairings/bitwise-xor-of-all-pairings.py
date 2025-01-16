class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        if n2 % 2 == 0 and n1%2==0:
            return 0
        if n2 % 2 == 0 and n1%2!=0:
            ans = 0
            for i in nums2:
                ans ^= i
            return ans
        if n1%2==0 and n2%2!=0:
            ans = 0
            for i in nums1:
                ans ^= i
            return ans
        ans = 0
        for i in nums1:
            ans ^= i

        for i in nums2:
            ans ^= i
        return ans
        

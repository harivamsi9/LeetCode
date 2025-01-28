class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if the rotation is 0 times, then return nums[0]
        if nums[0] < nums[-1]: return nums[0]
        if len(nums) == 1: return nums[0]

        # we need to find the index
        # where arr[i] < arr[i+1] => then return arr[i+1]
        # or arr[i-i] > arr[i] => then return arr[i]

        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = start + (end - start) // 2

            if mid+1 < len(nums) and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif mid-1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[start] > nums[mid]:
                end = mid - 1
            elif mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                start = mid+1
            else:
                end = mid - 1
        
        return nums[start]



        
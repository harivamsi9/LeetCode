class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 0:
            return -1
        # find pivot index
        def findPivot(nums):
            if nums[0] < nums[-1]: return 0
            start = 0
            end = len(nums) - 1

            while (start <= end):
                mid = start + (end- start) // 2
                if mid+1 < len(nums) and nums[mid] > nums[mid+1]: return mid
                elif mid-1 >= 0 and nums[mid] < nums[mid-1]: return mid-1
                elif nums[start] < nums[mid]: start = mid + 1
                else: end = mid - 1
            return end
        pivotIdx = findPivot(nums)

        print("pivotIdx: ", pivotIdx)

        # bs
        def binarySearch(nums, target, start, end):
            
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target: return mid
                elif nums[mid] < target: start = mid + 1
                else: end = mid - 1
            return -1
        # apply BS on left side
        left = binarySearch(nums, target, 0, pivotIdx)
        if left != -1:
            return left
        # Apply BS on right side 

        return binarySearch(nums, target, pivotIdx+1, len(nums)-1)

        
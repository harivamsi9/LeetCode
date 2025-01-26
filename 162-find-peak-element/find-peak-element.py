class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2
            
            # Check if mid is the peak element
            # Check left and right boundaries if they exist
            left = arr[mid - 1] if mid - 1 >= 0 else float('-inf')
            right = arr[mid + 1] if mid + 1 < len(arr) else float('-inf')
            
            if arr[mid] > left and arr[mid] > right:
                # Peak found
                return mid
            elif arr[mid] > left:
                # Move to the right side
                start = mid + 1
            else:
                # Move to the left side
                end = mid - 1
        
        # In theory, we shouldn't reach here because a peak will always be found.
        return -1

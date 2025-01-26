class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:


        def binarySearch(arr, target, findFirstPos=False):

            start = 0
            end = len(arr) - 1

            ans = -1

            while start <= end:
                mid = start + (end-start) // 2

                if target < arr[mid]: end = mid - 1
                elif target > arr[mid]: start = mid + 1
                else:
                    # potential ans is found
                    ans = mid
                    if findFirstPos:
                        end = mid - 1
                    else:
                        start = mid + 1

            return ans
        
        first_idx = binarySearch(arr, target, True)
        last_idx = binarySearch(arr, target)


        return [first_idx, last_idx]
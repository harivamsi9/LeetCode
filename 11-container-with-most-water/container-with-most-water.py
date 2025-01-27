class Solution:
    def maxArea(self, arr: List[int]) -> int:
        start = 0 
        end = len(arr) - 1
        max_area = 0
        while (start < end):
            dist = end - start
            height = min(arr[start], arr[end])
            area = dist * height
            max_area = max(max_area, area)

            if arr[start] < arr[end]:
                start += 1
            else:
                end -= 1
        return max_area
        
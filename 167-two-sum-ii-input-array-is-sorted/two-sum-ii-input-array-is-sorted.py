class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        start = 0
        end = len(arr) - 1
        while (start < end):

            if arr[start] + arr[end] == target:
                return [start+1, end+1]
            elif arr[start] + arr[end] < target:
                start += 1
            else:
                end -= 1
        return [-1,-1]
        
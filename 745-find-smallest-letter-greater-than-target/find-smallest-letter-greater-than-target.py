class Solution:
    def nextGreatestLetter(self, arr: List[str], target: str) -> str:
        if target >= arr[-1]: return arr[0]
        
        start, end = 0, len(arr) - 1

        while (start <= end):
            mid = (start+end) // 2
            if target < arr[mid]: end = mid - 1
            else: start = mid + 1

        if start > len(arr) - 1:
            return arr[0]
        return arr[start]
        
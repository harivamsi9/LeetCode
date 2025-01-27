class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        buy = arr[0]
        maxP = 0
        for i in range(1, len(arr)):
            p = arr[i]-buy
            maxP = max(p, maxP)
            buy = min(buy, arr[i])
        return maxP
            

        
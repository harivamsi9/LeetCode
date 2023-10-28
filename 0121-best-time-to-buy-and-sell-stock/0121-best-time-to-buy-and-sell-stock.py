class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProf = -9999999
        minValue = 9999999


        for j in range(1,len(prices)):
            # for i in range(0,j):
            minValue = min(prices[j-1], minValue)
            maxProf = max(maxProf, prices[j]-minValue)

        if maxProf < 0:
            return 0
        return maxProf

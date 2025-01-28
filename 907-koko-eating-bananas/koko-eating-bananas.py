class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = -1

        while (start <= end):
            mid = (start + end) // 2

            countHrs = 0
            for p in piles:
                if p!=0 and p%mid==0:
                    countHrs += p//mid
                else:
                    countHrs += p//mid + 1
            
            if countHrs <= h:
                ans = mid # one possible ans
                end = mid - 1
            else:
                start = mid + 1
        return ans

        
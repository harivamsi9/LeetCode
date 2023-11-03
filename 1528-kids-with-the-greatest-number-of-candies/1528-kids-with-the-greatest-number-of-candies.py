class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # brute force
        ans= []
        max_c = 0

        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies)
            max_c = max(candies[i], max_c)

        for i in range(len(candies)):
            if ans[i] >= max_c:
                ans[i] = bool(1)
            else:
                ans[i] = bool(0)
        return ans

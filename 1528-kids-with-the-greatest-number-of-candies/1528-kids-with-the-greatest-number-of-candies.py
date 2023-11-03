class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # # brute force TC: O(2N) SP: O(N)
        # ans= []
        # max_c = 0
        # for i in range(len(candies)):
        #     ans.append(candies[i] + extraCandies)
        #     max_c = max(candies[i], max_c)
        # for i in range(len(candies)):
        #     if ans[i] >= max_c:
        #         ans[i] = True
        #     else:
        #         ans[i] = False
        # return ans

        ## Space Optimized:: TC: O(2N) SP: O(1)
        ## Loop once, and get the max from the candies list.
        ## In 2nd loop, check if candies[i]+extraCandies >= max
        ## and update
        # max_c = max(candies)
        # for i in range(len(candies)):
        #     if candies[i] + extraCandies >= max_c:
        #         candies[i] = True
        #     else:
        #         candies[i] = False
        # return candies

        check=max(candies)-extraCandies
        return [k>=check for k in candies]






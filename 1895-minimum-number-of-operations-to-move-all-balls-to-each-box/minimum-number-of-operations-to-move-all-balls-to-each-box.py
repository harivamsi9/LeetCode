# Approach:
# 1. Convert the input string to a list of integers for easier manipulation.
# 2. Compute prefix sums (ps):
#    - For each index, calculate the cumulative sum of operations required to move all '1's from the start to that index.
# 3. Compute suffix sums (ss):
#    - For each index, calculate the cumulative sum of operations required to move all '1's from the end to that index.
# 4. Calculate the final answer:
#    - For each index, the result is the sum of prefix and suffix contributions at that index (ps[i] + ss[i]).
# 5. Return the resulting list of operations for each position.

class Solution:
    def minOperations(self, arr: str) -> List[int]:
        # Prefix Sum Method 
        # TC - O(n), SC - O(n)
        arr = [int(i) for i in arr]

        ps = [0] * len(arr)
        ss = [0] * len(arr)
        ans = [0] *len(arr)

        c = arr[0]
        ps[0] = 0
        for i in range(1, len(arr)):
            ps[i] += ps[i-1] + c
            c += arr[i]

        c = arr[-1]
        ss[-1] = 0
        for i in range(len(arr)-1 -1,-1,-1):
            ss[i] += ss[i+1] + c
            c += arr[i]

        for i in range(len(arr)):
            ans[i] = ps[i] + ss[i]

        return ans


        
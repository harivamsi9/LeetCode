class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        ans = [0]
        max_sum = 0
        for i in range(len(gain)):
            new = ans[-1] + gain[i]
            max_sum = max(max_sum, new)
            ans.append(new)

        return max_sum

        
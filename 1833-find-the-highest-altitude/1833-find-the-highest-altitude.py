class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # ## Brute Force TC: O(N) SC: (N)
        # ans = [0]
        # max_sum = 0
        # for i in range(len(gain)):
        #     new = ans[-1] + gain[i]
        #     max_sum = max(max_sum, new)
        #     ans.append(new)
        # return max_sum

        # Space Optimized TC: O(N), SC: O(1)
        max_sum = max(0,gain[0])
        for i in range(1, len(gain)):
            gain[i] = gain[i] + gain[i-1]
            max_sum = max(gain[i], max_sum)
        return max_sum



        
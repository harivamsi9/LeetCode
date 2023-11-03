class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_amt = 0

        for i in accounts:
            max_amt = max(sum(i),max_amt)

        return max_amt
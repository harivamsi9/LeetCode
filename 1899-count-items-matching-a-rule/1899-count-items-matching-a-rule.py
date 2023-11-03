class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Brute Force
        first = "type"
        second = "color"
        third = "name"
        k = 0
        count = 0
        if ruleKey == first:
            # pass
            k = 0

        elif ruleKey == second:
            # pass
            k = 1
        else:
            # name
            k =2
            
        for i in range(len(items)):
            if items[i][k] == ruleValue:
                count+=1
        return count
        
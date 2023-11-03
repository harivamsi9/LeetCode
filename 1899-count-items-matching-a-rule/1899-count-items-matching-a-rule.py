class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Brute Force
        k = 0
        count = 0
        if ruleKey[0] == 'c':
            # color
            k = 1
        elif ruleKey[0]=='n':
            # name
            k =2
            
        for i in range(len(items)):
            if items[i][k] == ruleValue:
                count+=1
        return count
        
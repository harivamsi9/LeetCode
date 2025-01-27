class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            self.checkInclusion(s2,s1)
        # now len(s1) < len(s2)
        windowSize = len(s1)
        count = {}
        for i in range(len(s1)):
            if s1[i] in count:
                count[s1[i]] += 1
            else:
                count[s1[i]] = 1

        for i in range(len(s2) - windowSize + 1):
            sub_arr = s2[i:i+windowSize]
            counterS2 = Counter(sub_arr)
            if count == counterS2: return True
            counterS2[s2[i]] -= 1
        return False


            

        
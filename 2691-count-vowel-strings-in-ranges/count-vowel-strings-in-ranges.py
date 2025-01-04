class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelCount = [0]*len(words)
        for i, word in enumerate(words):
            if word[-1] in "aeiou" and word[0] in "aeiou":
                vowelCount[i] += 1

        ps = [0]*len(words)
        ps[0] = vowelCount[0]
        for i in range(1,len(words)):
            ps[i] += ps[i-1] + vowelCount[i]
        
        ans = []
        for q in queries:
            l,r = q
            rval = ps[r]
            lval = 0
            if l > 0:
                lval = ps[l-1]
            ans.append(rval-lval)
        return ans
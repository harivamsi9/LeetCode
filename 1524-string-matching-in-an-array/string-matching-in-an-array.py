class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def isSubstr(s: str, t:str)->bool:
            return t in s

        ans = set()
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if isSubstr(words[i], words[j]):
                    ans.add(words[j])
                elif isSubstr(words[j], words[i]):
                    ans.add(words[i])
        return list(ans)
                
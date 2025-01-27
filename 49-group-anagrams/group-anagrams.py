class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {} # count seq -> list of strs

        for i in range(len(strs)):
            count = [0] *26
            s = strs[i]
            for j in s:
                count[ord(j) - ord('a')] += 1
            if tuple(count) in hashmap:
                hashmap[tuple(count)].append(s)
            else:
                hashmap[tuple(count)] = [s]

        return list(hashmap.values())
        
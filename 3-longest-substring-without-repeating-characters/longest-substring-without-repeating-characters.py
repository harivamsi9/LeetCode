class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        l = 0
        r = 1
        dict_ = {}
        max_len = 1

        dict_[s[l]] = 1

        while r < len(s):
            if s[r] in dict_:
                del dict_[s[l]]
                l += 1
            else:
                dict_[s[r]] = 1
                r += 1
            max_len = max(max_len, r-l)
        return max_len


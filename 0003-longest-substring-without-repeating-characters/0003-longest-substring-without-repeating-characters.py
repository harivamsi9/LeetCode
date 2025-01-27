class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force:  TC: O(N^2), SC: O(N*(N+1)/2)=O(N^2)
        '''
        Starting at each index, check the max you can go without repeating the characters
        '''
        # max_len = 1
        # for i in range(len(s)-1):
        #     leng = 0
        #     for j in range(i+1, len(s)):
        #         subStr = s[i:j]
        #         set_ = set(subStr)
        #         if len(subStr) == len(set_):
        #             leng +=1 
        #         else:
        #             break
        #     max_len = max(max_len, leng)
        # return max_len

        # Time Optimized: 
        # ''''
        # s = "abfdfcabcbb"
        # abc, i = 0, j = 2, max = 3
        # (0,3, 3) -> abca
        #     if s[i] == s[j]: del dict[s[i]]; 
        #     i++ -> (1,3)
        #         bca
        # (1,3, 3) -> bca
        #     j++
        # (1,4,3) -> bcab
        #     if s[i] == s[j]: del dict[s[i]]; 
        #     i++ -> (2,4)
        #         cab
        # (2,4,3) -> cab
        #     j++
        # (2,5,3) -> cab
        # ''''
        if len(s) == 0:
            return 0

        max_len = 1
        n = len(s)
        i = 0 
        j = 1
        dict_ = {}
        dict_[s[i]] = 1
        # tmmzuxt
        while (j < n):
            # check if repeating
            # print(s[i:j])
            if s[j] in dict_:
                # check if s[i] is s[j]
                # print(dict_, i,j)
                # if s[i] == s[j]:
                del dict_[s[i]]
                i += 1

            else:
                dict_[s[j]] = 1
                # dict_[s[i]] = 1
                j+=1
            max_len = max(max_len, j-i)

        return max_len


        
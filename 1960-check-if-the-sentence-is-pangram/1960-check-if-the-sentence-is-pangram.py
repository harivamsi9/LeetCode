class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Brute Force TC: O(N^2) SC: O(1)
        # check = 'qwertyuiopasdfghjklzxcvbnm'
        # for letter in check:
        #     if letter not in sentence:
        #         return False
        # return True

        # # Optimized Solution TC: O(N) SC: O(N)
        # dict_1 = {}
        # for s in sentence:
        #     dict_1[s] = 1
        # if len(dict_1.keys()) != 26:
        #     return False
        # return True

        return len(set(sentence)) == 26
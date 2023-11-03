class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check = 'qwertyuiopasdfghjklzxcvbnm'

        for letter in check:
            if letter not in sentence:
                return False

        return True
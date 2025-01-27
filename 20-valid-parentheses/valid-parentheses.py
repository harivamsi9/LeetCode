class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")" : "(", 
            "}" : "{", 
            "]" : "["
        }
        stack = []

        for i in s:
            if i in d:
                if len(stack) > 0 and stack[-1] == d[i]:
                    stack.pop()
                else:
                    # stack.append(i)
                    return False
            else:
                stack.append(i)
        if stack: return False
        return True


        
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0] * len(temp)
        if len(temp) == 0:
            return []

        stack = [(temp[0],0)]
        for i in range(1,len(ans)):
            while len(stack) != 0 and stack[-1][0] < temp[i]:
                # you can pop the stack
                t, j = stack.pop()
                ans[j] = i-j
            stack.append((temp[i], i))
        return ans




        
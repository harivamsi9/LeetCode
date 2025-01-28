class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append( (position[i], speed[i]) )
        arr = sorted(arr, reverse=True)
        stack = []
        for i in range(len(arr)):
            t = (target - arr[i][0])/arr[i][1]

            curr = (arr[i][0], arr[i][1], t)

            if len(stack) != 0:
                if curr[2] > stack[-1][2]:
                    stack.append(curr)
            else:
                stack.append(curr)
        return len(stack)



        
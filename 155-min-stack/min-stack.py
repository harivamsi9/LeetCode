class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            minTop = self.minstack[-1]
            self.minstack.append(min(minTop, val))

    def pop(self) -> None:
        if len(self.stack) > 0:
            # you can remove
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack) > 0:
            return self.minstack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
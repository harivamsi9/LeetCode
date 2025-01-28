class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if not(token in "+-/*"):
                stack.append(int(token))
            else:
                if len(stack) > 1:
                    rightOp = stack.pop()
                    leftOp = stack.pop()
                    print(f"left: {leftOp} {token} right: {rightOp}")
                    if token == "+":
                        stack.append(rightOp+leftOp)
                    elif token == "-":
                        stack.append(leftOp - rightOp)
                    elif token == "/":
                        stack.append(int(leftOp/rightOp))
                    else:
                        stack.append(leftOp*rightOp)
        # print(stack)
        return stack.pop()
        
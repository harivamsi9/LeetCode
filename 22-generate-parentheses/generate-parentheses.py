class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        ds = []

        def backtrack(openB, closeB):
            if openB == closeB == n:
                ans.append(''.join(ds))
                return
            
            if openB < n:
                # call '('
                ds.append('(')
                backtrack(openB + 1, closeB)
                ds.pop()
            
            if closeB < openB and closeB < n:
                ds.append(')')
                backtrack(openB, closeB + 1)
                ds.pop()
        backtrack(0,0)
        return ans

            



        
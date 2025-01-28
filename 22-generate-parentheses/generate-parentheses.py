class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(ds, openB, closeB):
            if openB == closeB == n:
                ans.append(''.join(ds))
                return
            
            if openB < n:
                # call '('
                ds.append('(')
                backtrack(ds.copy(), openB + 1, closeB)
                ds.pop()
            
            if closeB < openB and closeB < n:
                ds.append(')')
                backtrack(ds.copy(), openB, closeB + 1)
                ds.pop()
        backtrack([],0,0)
        return ans

            



        
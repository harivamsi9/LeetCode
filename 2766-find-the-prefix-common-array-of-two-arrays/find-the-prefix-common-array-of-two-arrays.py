class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        ac = [0]*51
        bc = [0]*51

        ans = []
        
        for i in range(len(A)):
            ac[A[i]] += 1
            bc[B[i]] += 1

            c = 0
            
            for j in range(len(ac)):
                if ac[j] > 0 and bc[j] > 0: c += min(ac[j],bc[j])

            ans.append(c)

        return ans


            
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p,n,z=[],[],[]
        res = set()
        p_,n_ = set(),set()
        for i in nums:
            if i == 0:
                z.append(i)
            elif i > 0:
                p.append(i)
                p_.add(i)
            else:
                n.append(i)
                n_.add(i)

        # (0,-x,x)
        if len(z) > 0:
            for i in p_:
                if -1*i in n_:
                    res.add((-1*i,0,i))
        # (0,0)
        if len(z) > 2:
            res.add((0,0,0))
        

        # (sum(x1,x2), -x3)
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if (p[i]+p[j])*-1 in n_: res.add(tuple(sorted([(p[i]+p[j])*-1,p[i],p[j]])))

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if (n[i]+n[j])*-1 in p_: res.add( tuple(sorted([(n[i]+n[j])*-1,n[i],n[j]])))

        return list(res)
        
        
        
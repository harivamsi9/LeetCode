class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = []
        cc = {} # freq -> set(unique nums)
        for kk,v in c.items():
            if v in cc:
                cc[v].add(kk)
            else:
                cc[v]=set()
                cc[v].add(kk)

        max_k = len(nums)
        while (max_k > 0 and k > 0):
            if max_k in cc and k>0:
                arr = cc[max_k]
                for a in arr:
                    ans.append(a)
                    k -= 1
            max_k -= 1

        return ans


        
class Solution:
    def minOperations(self, arr: str) -> List[int]:
        arr = [int(i) for i in arr]

        ps = [0]*len(arr)
        ss = [0] * len(arr)
        ans = [0] *len(arr)

        c = arr[0]
        ps[0] = 0
        for i in range(1, len(arr)):
            ps[i] += ps[i-1] + c
            c += arr[i]
        print(ps)

        c = arr[-1]
        ss[-1] = 0
        for i in range(len(arr)-1 -1,-1,-1):
            ss[i] += ss[i+1] + c
            c += arr[i]
        print(ss)

        for i in range(len(arr)):
            ans[i] = ps[i] + ss[i]

        return ans


        
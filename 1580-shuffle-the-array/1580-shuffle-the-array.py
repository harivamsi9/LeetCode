class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # ans = [0]*2*n
        ans = []
        i = 0
        j = n
        while i < n:
            # ans[i] = nums[i]
            ans.append(nums[i])
            ans.append(nums[j])
            # ans[i+1] = nums[j]
            i +=1
            j +=1

        return ans

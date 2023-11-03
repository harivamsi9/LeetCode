class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # approach 1
        # ans = []
        # i = 0
        # j = n
        # while i < n:
        #     # ans[i] = nums[i]
        #     ans.append(nums[i])
        #     ans.append(nums[j])
        #     # ans[i+1] = nums[j]
        #     i +=1
        #     j +=1
        # return ans

        # Approach 2 TC-> O(N), SC-> O(N)
        # ans= [0]*2*n
        # for i in range(n):
        #     # even indexes
        #     ans[2*i] = nums[i]
        #     # odd indexes
        #     ans[2*i+1] = nums[i+n]

        # return ans
        
        # Space Optimized
        # [2,5,1,3,4,7] -> [2,3,5,4,1,7]
        # meta = a + b * c
        # a = num[i]
        # b = num[i+n] % c
        c = 1001

        for i in range(n):
            # Calculate the index of y(i)
            idx_y = i + n
            # Store the y(i) element temporarily
            temp = nums[idx_y]
            
            # Shift the elements to create space for x(i) at odd indices
            for j in range(idx_y, i * 2, -1):
                nums[j] = nums[j - 1]
            
            # Place x(i) and y(i) at their correct positions
            nums[i * 2 + 1] = temp
        
        return nums







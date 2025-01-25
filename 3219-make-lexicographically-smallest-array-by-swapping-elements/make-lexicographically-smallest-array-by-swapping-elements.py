# class Solution:
#     def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
#         # sort the array
#         # maintain a visited array
#         # maintain a hashmap to store the elemt and its indexes
#         # 
#         # loop i := 0 -> len(arr)-1
#         #   curr = arr[i]
#         #   bsCurrIndex = use binarySearch to find curr in the sorted array
#         #   go to the left of bsCurrIndex in the sorted array and check 
#         #   if there are any elemts smaller than curr and abs(curr, leftElemt) <= limit
#         #   Do the above in a while loop till you find the smallest && unvisited value
#         #   Swap
#         import bisect

#         sorted_arr = sorted(nums)
#         visited = [0]*len(nums)
#         ans = [0]*len(nums)
#         valIndex = {}
#         for idx, val in enumerate(nums):
#             if val in valIndex:
#                 valIndex[val].append(idx)
#             else:
#                 valIndex[val] = [idx]

#         for i in range(len(nums)):
#             curr = nums[i]
#             # bsCurrIndex = binarySearch(sorted_arr)
#             bsCurrIndex = bisect.bisect_left(sorted_arr, curr)
#             smallest = nums
#             j = i
#             while j>=0 and  




class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        nums_sorted = sorted(nums)

        curr_group = 0
        num_to_group = {}
        num_to_group[nums_sorted[0]] = curr_group

        group_to_list = {}
        group_to_list[curr_group] = deque([nums_sorted[0]])

        for i in range(1, len(nums)):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                # new group
                curr_group += 1

            # assign current element to group
            num_to_group[nums_sorted[i]] = curr_group

            # add element to sorted group deque
            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])

        # iterate through input and overwrite each element with the next element in its corresponding group
        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums
        
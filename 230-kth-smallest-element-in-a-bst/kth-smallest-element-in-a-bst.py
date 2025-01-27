# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, count, k):
            if not root: return -1
            # in-order
            left = dfs(root.left, count, k)
            if left!= None and left >= 0:
                return left

            self.count += 1

            if self.count == k:
                return root.val

            right = dfs(root.right, count, k)
            if right != None and right >= 0: return right


        return dfs(root, count, k)
        
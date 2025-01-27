# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lb, rb):
            if root == None:
                return True
            if not(lb < root.val < rb): return False

            left = dfs(root.left, lb, min(rb, root.val))
            right = dfs(root.right, max(lb, root.val), rb)

            return left and right

        return dfs(root, float('-inf'), float('inf'))

        
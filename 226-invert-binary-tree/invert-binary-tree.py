# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if root == None:
                return None
            left = dfs(root.left)
            right = dfs(root.right)
            root.left = right
            root.right = left
            return root

        dfs(root)
        return root
        
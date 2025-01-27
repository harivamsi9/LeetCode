# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path):
            if not root:
                return

            if root.left == None and root.right == None:
                # leaf node
                path += str(root.val)
                self.ans += int(path)
                return

            left = dfs(root.left, path + str(root.val))
            right = dfs(root.right, path + str(root.val))

        dfs(root, "")
        return self.ans

        
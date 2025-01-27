# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum):
            if root == None:
                return False
            # if targetSum < 0:
            #     return False
            
            if root.left == None and root.right == None:
                # leaf node
                if targetSum == root.val:
                    return True
                return False
                
            
            left = dfs(root.left, targetSum-root.val)
            if left: return left
            right = dfs(root.right, targetSum-root.val)
            if right: return right
            return False



        
        return dfs(root, targetSum)
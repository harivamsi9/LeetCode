# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathSum = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currSum):
            if not root: return False
            currSum += root.val
            if not root.left and not root.right:
                return currSum == targetSum
            return dfs(root.left,currSum) or dfs(root.right, currSum)

        return dfs(root,0)



        # # DFS
        # if not root:
        #     return False
        # stack = [(root, root.val)]
        # while stack:

        #     node, sum_val = stack.pop()

        #     if not node.left and not node.right: # leaf Node
        #         if sum_val == targetSum:
        #             return True

        #     if node.right:
        #         stack.append( (node.right, sum_val + node.right.val) )
            
        #     if node.left:
        #         stack.append((node.left, sum_val + node.left.val))

        # return False
        
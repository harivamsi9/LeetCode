# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        ans = []
        while queue:
            levelSize = len(queue) # 1
            for i in range(levelSize): # 0
                node = queue.pop(0)
                if i == levelSize - 1:
                    if node:
                        ans.append(node.val)
                if node and node.left: queue.append(node.left)
                if node and node.right: queue.append(node.right)
                
        return ans 
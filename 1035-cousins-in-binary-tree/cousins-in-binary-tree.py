# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root == None or root ==[]: return False
        queue = [root]
        while queue:
            levelSize = len(queue)
            xPresent = False
            xLoc = 0
            yLoc = 0
            yPresent = False
            for i in range(levelSize):
                node = queue.pop(0)
                if node.val == x: 
                    xPresent = True
                if node.val == y:
                    yPresent = True
                if node.left and node.right and node.left.val == x and node.right.val == y: return False
                if node.left and node.right and node.left.val == y and node.right.val == x: return False
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if xPresent and yPresent: return True




        return False

        
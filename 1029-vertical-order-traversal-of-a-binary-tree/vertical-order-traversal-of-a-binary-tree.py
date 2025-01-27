# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict_ = {} # vlevel: int -> List[int]
        # dict_[0] = [root.val]
        queue = [(root, 0, 0)] # (root, vlevel)

        while queue:

            levelSize = len(queue)

            for i in range(levelSize):
                node, vlevel, depth = queue.pop(0)
                if vlevel in dict_:
                    dict_[vlevel].append((depth,node.val))
                else:
                    dict_[vlevel] = [(depth,node.val)]
                # add nodes to queue
                if node.left:
                    queue.append((node.left, vlevel - 1, depth + 1))
                if node.right:
                    queue.append((node.right, vlevel + 1, depth + 1))
        
        keys = sorted(dict_.keys())
        res = []
        for k in keys:
            row = []
            for depth, val in sorted(dict_[k]):
                row.append(val)
            res.append(row)
        return res





        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)

    def getDepth(self, node):
        if node is None:
            return 0
        leftheight = self.getDepth(node.left)
        rightheight = self.getDepth(node.right)
        height = 1 + max(leftheight,rightheight)
        return height
        
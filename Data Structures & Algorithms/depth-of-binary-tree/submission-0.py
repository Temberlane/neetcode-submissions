# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        if root.left is not None:
            left_max = 1 + self.maxDepth(root.left)
        else:
            left_max = 0
        if root.right is not None:
            right_max = 1 + self.maxDepth(root.right)
        else:
            right_max = 0

        return max(left_max, right_max)
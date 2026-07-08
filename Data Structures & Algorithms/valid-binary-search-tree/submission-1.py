# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            # left subtree and right subtree valid val comparison
            if not (node.val < right and node.val > left):
                return False
            # left subtree must be less than parent - set as right boundary
            # right subtree must be greater than parent - set as left boundary
            # node is whats being checked
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
        return valid(root, float("-inf"), float("inf"))
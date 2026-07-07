# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both empty they are the same
        if not p and not q:
            return True
        # if one is and one isn't empty then false
        if not p or not q:
            return False
        # check the vals of root before moving on
        if p.val != q.val:
            return False
        
        # and check so if one is true but one is false then false
        # recursion to check right and left sides of tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
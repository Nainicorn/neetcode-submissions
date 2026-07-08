# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case - ret null or 1 elem
        if not preorder or not inorder:
            return None
        # get first elem of preorder
        # list of ints so need to do this
        root = TreeNode(preorder[0])
        # needed to figure out whats in left and whats in right subtree
        mid = inorder.index(preorder[0])
        # recursive case
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
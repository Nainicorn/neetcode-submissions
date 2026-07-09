# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs recursion
        def dfs(node):
            if not node:
                # index 0 bool index 1 val
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            
            # if left and right are both balanced - true
            # if entire tree is balanced from root/start
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


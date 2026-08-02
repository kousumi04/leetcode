# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self, root, p, q):    
        if root is None:
            return None
        if root==p or root==q:
            return root
        left=self.solve(root.left,p,q)
        right=self.solve(root.right,p,q)
        # if left is None or right is None:
        #     return None
        if left is None:
            return right
        if right is None:
            return left
        return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root, p, q)
        
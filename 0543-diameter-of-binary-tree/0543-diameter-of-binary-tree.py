# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0  # holds the maximum diameter found

    def calculateHeight(self, root):
        # Base case: empty tree has height 0
        if not root:
            return 0

        # Recursively find heights of left and right subtrees
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)

        # Update diameter: path through root uses leftHeight + rightHeight edges
        self.diameter = max(self.diameter, leftHeight + rightHeight)

        # Return the height of this subtree (in nodes)
        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize diameter and start recursion
        self.diameter = 0
        self.calculateHeight(root)
        return self.diameter
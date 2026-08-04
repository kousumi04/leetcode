# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        queue=deque([root])    
        while queue:
            right=None
            level_size=len(queue)
            for _ in range(level_size):    
                node=queue.popleft()
                if node:
                    right=node
                    queue.append(node.left)
                    queue.append(node.right)
            if right:        
                res.append(right.val)
        return res        



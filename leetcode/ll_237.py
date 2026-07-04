class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
node=Solution(4)
node.next=Solution(5)
node.next.next=Solution(1)
node.next.next.next=Solution(9)
node.next.next.next.next=Solution(3)
s=Solution()
new_head=s.deleteNode(node)
curr = node
while curr:
    print(curr.val, end=" ")
    curr = curr.next        
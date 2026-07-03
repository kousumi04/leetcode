# class Solution:
#     # def __init__(self, val=0, next=None):
#     #     self.val = val
#     #     self.next = next
#     def middleNode(self, head):
#         count=0
#         cur=head
#         while cur!=None:
#             cur=cur.next
#             count+=1
#         # return count
#         cur=head
#         for i in range(count//2):
#             cur=cur.next
#         return cur 



#optimized version using slow and fast pointer

class Solution:
    def middleNode(self, head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        prev=None
        if head==None or head.next==None:
            return head
        while fast and fast.next:
            # find middle 
            prev=slow
            slow=slow.next
            fast=fast.next.next
        # split  
        right=slow
        prev.next=None    

        left=self.sortList(head)
        right=self.sortList(right)
        # merge
        return self.merge(left, right)
    def merge(self, left, right):
        dummy=ListNode(0)
        tail=dummy
        while right and left:
            if left.val<right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if left:
            tail.next=left
        else:
            tail.next=right
        return dummy.next    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverseList(head):
            curr=head
            prev=None
            nxt=None
            while curr!=None:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev    

        slow=fast=head 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next 
        if fast:
            slow=slow.next
        first=head
        second=reverseList(slow)
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next    
        return True    

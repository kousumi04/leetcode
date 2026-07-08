class Solution:
    def isPalindrome(self, head):
        if head ==None or head.next==None:
            return head
        # find middle elemnet
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse the second half(from the middle)
        cur=slow
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        #compare both the sides 
        left=head
        right=head
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True        

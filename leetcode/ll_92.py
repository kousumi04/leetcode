class Solution:
    def reverseBetween(self, head, left, right):
        while head==None and left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        before=dummy
        for i in range(left-1):
            before=before.next
            # start reversing the position left
        cur=before.next
        prev=None
        for i in range(right-left+1):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        #reconnect the reversed portion
        before.next.next=cur
        before.next=prev 
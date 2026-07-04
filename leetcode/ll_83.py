class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def deleteDuplicates(self, head):
        cur=head
        # edge cases
        if head==None or head.next==None:
            return head
        while cur!=None and cur.next!=None:
            if cur.next.val==cur.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head    
head=Solution(1)
head.next=Solution(1)
head.next.next=Solution(2)
head.next.next.next=Solution(3)
head.next.next.next.next=Solution(3)
s=Solution()
new_head=s.deleteDuplicates(head)
curr = head
while curr:
    print(curr.val, end=" ")
    curr = curr.next    
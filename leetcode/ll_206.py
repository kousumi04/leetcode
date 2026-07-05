class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverseList(self, head):
        cur=head
        prev=None
        nxt=None
        while cur!=None :
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev    
             
head=Solution(1)
head.next=Solution(2)
head.next.next=Solution(3)
head.next.next.next=Solution(4)
head.next.next.next.next=Solution(5)
s=Solution()
new_head=s.reverseList(head)
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next        
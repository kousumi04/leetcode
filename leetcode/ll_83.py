class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def deleteDuplicates(self, head):
        slow=head
        fast=head
        res=[]
           
head=Solution(1)
head.next=Solution(1)
head.next.next=Solution(2)
head.next.next.next=Solution(3)
head.next.next.next.next=Solution(3)
s=Solution()
new_head=s.deleteDuplicates(head)
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next    
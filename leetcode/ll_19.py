class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def removeNthFromEnd(self, head, n):
        slow=head
        fast=head
        for i in range(n):
            fast=fast.next

        if fast==None:
            head=head.next
            return head
        while fast.next!=None :
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next  
        return head  

head=Solution(1)
head.next=Solution(2)
head.next.next=Solution(3)
head.next.next.next=Solution(4)
head.next.next.next.next=Solution(5)
s=Solution()
new_head=s.removeNthFromEnd(head,2)
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
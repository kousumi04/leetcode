class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def rotateRight(self, head, k):
        if head==None or head.next==None:
            return head
        l=0
        last=head
        while last!=None:
            last=last.next
            l+=1
        l+=1
        k=k%l
        if k==0:
            return head
        cur=head
        for i in range(l-k-1):
            cur=cur.next
        last.next=head    
        head=cur.next
        cur.next=None

        return head
             
head=Solution(1)
head.next=Solution(2)
head.next.next=Solution(3)
head.next.next.next=Solution(4)
head.next.next.next.next=Solution(5)
s=Solution()
new_head=s.rotateRight(head,2)
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
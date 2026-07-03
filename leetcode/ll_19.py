class Solution:
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
s=Solution()
head = [1,2,3,4,5]
n = 2
print(s.removeNthFromEnd(head, n))
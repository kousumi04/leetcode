class Solution:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev=prev
    def deleteDuplicates(self, head):
        fake_node=Solution(0)
        fake_node.next=head

        prev=fake_node
        cur=head
        
        while cur:
            if cur.next and cur.val==cur.next.val:
                while cur.next and cur.next.val==cur.val:
                    cur=cur.next
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next

        return fake_node.next                
            
head=Solution(1)
head.next=Solution(1)
head.next.next=Solution(2)
head.next.next.next=Solution(3)
# head.next.next.next.next=Solution(3)
s=Solution()
new_head=s.deleteDuplicates(head)
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next    
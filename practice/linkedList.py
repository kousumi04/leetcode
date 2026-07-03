class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

# traverse a linkedlist
def printLinkedList(head):
    cur=head
    while cur!=None:
        print(cur.data, end="->")
        cur=cur.next
    print("None")   

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

#insertion at the beginning  
newNode=Node(50)
newNode.next=head
head= newNode

# insertion at the end
newNode=Node(60)
cur=head
while cur.next!=None:
    cur=cur.next
cur.next=newNode    

# insertion at the kth index
k=2
newNode=Node(70)
cur=head
for i in range(k-1):
    cur=cur.next
newNode.next=cur.next
cur.next=newNode    

# delete the first node
head=head.next

# delete the last node
cur=head
while cur.next.next!=None:
    cur=cur.next
cur.next=None   

# delete from the kth index
k=1
cur=head
for i in range(k-1):
    cur=cur.next
cur.next=cur.next.next    

printLinkedList(head)
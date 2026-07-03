class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
a=Node(10)
a.next=Node(20)
a.next.next=Node(30)
a.next.next.next=Node(40)
cur=a
# traverse a linkedlist
while cur:
    print(cur.data, end="->")
    cur=cur.next
print("None")    


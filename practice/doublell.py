class DoublyNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

a=DoublyNode(5)
b=DoublyNode(3)
c=DoublyNode(7)
a.next=b
b.prev=a
b.next=c    
head=a
print(head.data)
print(head.next.data)
print(head.next.next.data)

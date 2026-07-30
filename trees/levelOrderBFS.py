from collections import deque
class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None   

one=Node("1")
two=Node("2")
three=Node("3")
four =Node("4")
five=Node("5")
six=Node("6")
seven=Node("7")
two.left=four
two.right=five
three.left=six 
three.right=seven
one.left=two
one.right=three
def level_order(node):
    res=[]
    queue=deque([])
    queue.append(node)
    while len(queue)!=0:
        e=queue.popleft()
        res.append(e.val)
        if e.left is not None:
            queue.append(e.left)
        
        if e.right is not None:
            queue.append(e.right)   
    return res      
print(level_order(one))
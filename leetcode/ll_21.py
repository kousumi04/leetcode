class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
def createLinkedList(arr):
    dummy = ListNode()
    tail = dummy

    for x in arr:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next

def printLinkedList(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])
s = Solution()
new_head = s.mergeTwoLists(list1, list2)
printLinkedList(new_head)
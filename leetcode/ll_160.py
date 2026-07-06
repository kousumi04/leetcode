
class Solution:
    def getIntersectionNode(self, headA, headB):
        p1=headA
        p2=headB
        c=0
        while True:
            if p1==p2:
                return p1
            p1=p1.next
            p2=p2.next
            if p2==None:
                c+=1
                p2=headA
            if p1==None:
                p1=headB   
            if c>1:
                return None    
        
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        leftSum, rightSum=0, 0
        maximum=0
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        for i in range(0,k):
            leftSum+=cardPoints[i]
        maximum=leftSum
        rightInd=n-1
        for i in range(k-1, -1, -1):
            leftSum-=cardPoints[i]
            rightSum+=cardPoints[rightInd]
            maximum=max(maximum, leftSum+rightSum)
            rightInd-=1
        return maximum    
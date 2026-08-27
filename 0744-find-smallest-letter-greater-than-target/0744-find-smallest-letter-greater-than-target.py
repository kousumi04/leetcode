class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mini=float("inf")
        ans=letters[0]
        for i in range(len(letters)):
            diff=ord(letters[i])-ord(target)
            if diff>0 and diff<mini:
                mini=diff
                ans=letters[i]
        return ans
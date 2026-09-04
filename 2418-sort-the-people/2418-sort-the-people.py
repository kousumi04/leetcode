class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result=[]
        people=list(zip(heights, names))
        people.sort(reverse=True)
        for height, name in people:
            result.append(name)
        return result
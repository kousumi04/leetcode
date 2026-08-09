class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat=0
        start=0
        end=len(people)-1
        while start<end:
            if people[end]==limit:
                boat+=1
                end-=1
            else:
                s=people[start]+people[end]
                if s==limit:
                    start+=1
                    end-=1
                    boat+=1
                elif s>limit:
                    end-=1
                    boat+=1
                else:
                    start+=1
                    end-=1
                    boat+=1
        if start==end and people[end]<=limit:
            boat+=1
        return boat
        # return boat                            

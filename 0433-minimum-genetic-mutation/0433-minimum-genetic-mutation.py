class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank or len(bank)==0:
            return -1
        bankSet=set(bank)
        queue=deque()
        queue.append((startGene,0))
        while len(queue)!=0:
            curr_word, level=queue.popleft()
            if curr_word==endGene:
                return level
            for i in range(0,len(curr_word)):
                for ch in "ACGT":
                    if ch==curr_word[i]:
                        continue
                    new_word=curr_word[:i]+ch+curr_word[i+1:]
                    if new_word in bankSet:
                        queue.append((new_word, level+1))
                        bankSet.remove(new_word)
        return -1
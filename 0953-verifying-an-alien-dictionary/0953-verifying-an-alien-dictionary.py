class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank={}
        for i in range(len(order)):
            rank[order[i]]=i
        for i in range(len(words)-1):
            word1, word2=words[i], words[i+1]
            found=False
            minLength=min(len(word1), len(word2))
            for j in range(minLength):
                if rank[word1[j]]<rank[word2[j]]:
                    found=True
                    break
                elif rank[word1[j]]>rank[word2[j]]:
                    return False
                elif rank[word1[j]]==rank[word2[j]]:
                    continue   
            if not found and len(word1)>len(word2):
                return False    
        return True    
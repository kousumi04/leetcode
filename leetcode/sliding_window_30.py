class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_length=len(words[0])
        total_length=len(words)*word_length
        res=[]
        count={}
        for word in words:
            if word in count:
                count+=1
            else:
                count=1
        for i in range(word_length):
            left=i
            sub_count={}
            c=0

            for j in range(i,len(s)-word_length)
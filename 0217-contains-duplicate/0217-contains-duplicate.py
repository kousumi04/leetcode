class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for num_key in nums:
            if num_key in freq.keys():
                freq[num_key]+=1
            else:
                 freq[num_key]=1
        duplicate = False
        for values in freq.values():
            if values>1:
                duplicate = True
        return duplicate













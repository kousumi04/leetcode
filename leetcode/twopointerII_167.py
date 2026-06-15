class Solution:
    def twoSum(self, numbers, target):
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum==target:
                return [i+1,j+1]
            elif sum<target:
                i+=1
            elif sum>target:
                j-=1
        return -1
numbers=[2, 7, 11, 15]
# target=int(input("Enter target value: "))
target=9
s=Solution()
print(s.twoSum(numbers, target))     
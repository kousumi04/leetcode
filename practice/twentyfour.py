# # 1. reverse a number
# def reverseNumber(number):
#     number=str(number)
#     return str(number[::-1])

# number=int(input("Enter a number: "))
# print(reverseNumber(number))

# # 2. Palindrome number
# def palindromeNumber(number):
#     number=str(number)
#     palindrome=number[::-1]
#     if number==palindrome:
#         print(f"{number} is a palindrome number.")
#     else:
#         print(f"{number} is not a palindrome number.")

# number=int(input("Enter a number: "))
# palindromeNumber(number)

# # 3. Palindrom string
# def palindromeNumber(word):
#     palindrome=word[::-1]
#     if word==palindrome:
#         print(f"{word} is a palindrome string.")
#     else:
#         print(f"{word} is not a palindrome number.")

# word=input("Enter a string: ")
# palindromeNumber(word)

# 4. Check for prime number
# def checkPrimeNumber(number):
#     root=int(number**0.5)
#     if number<2:
#         return False
#     if number == 2:
#         return True
#     for i in range(2,root+1):
#         if number%i==0:
#             return False
        
#     return True


# number=int(input("Enter a number: ")) 
# if checkPrimeNumber(number):
#     print("prime")
# else:
#     print("non prime")   


# 5. Print prime number in a range
# def checkPrimeNumber(number):
#     root=int(number**0.5)
#     if number<2:
#         return False
#     if number == 2:
#         return True
#     for i in range(2,root+1):
#         if number%i==0:
#             return False
        
#     return True

# start= int(input("Enter a starting point:"))
# end= int(input("Enter a ending point:"))
# if start<end:
#     for number in range(start, end+1):
#         if checkPrimeNumber(number):
#             print(f"{number}", end=" ")        

# elif end<start:
#     for number in range(end, start+1):
#         if checkPrimeNumber(number):
#             print(f"{number}", end=" ") 
# else:
#     print("Invalid")            

# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i>5:
#         print(i)

# 6. count vowels in a string
# def countVowels(string):
#     vowels=[]
#     for i in string:
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             vowels=vowels+[i]
#     print(len(vowels))
# string=input("Enter a string: ")
# countVowels(string)


# def countVowels(word):
#     count=0
#     for i in word:
#         if i in "aeiou":
#             count+=1

#     print(count)

# string=input("Enter a string: ")
# countVowels(string)


# # print non-vowels
# def countNonVowels(word):
#     count=0
#     for i in word:
#         if i not in "aeiou":
#             count+=1

#     print(count)

# string=input("Enter a string: ")
# countNonVowels(string)


# Find largest element (array)
# def largestElement(arr):
#     if len(arr)<=1:
#         return arr
#     sorted_arr=[]
#     pivot=arr[0]
#     left= [x for x in arr[1:] if x<=pivot]
#     right=[x for x in arr[1:] if x>pivot]
#     return largestElement(left)+[pivot]+largestElement(right)
    
# arr=input("Enter values: ").split()
# arr=largestElement(arr)

# print(arr[-1])


# Sum of elements (array)
# def sumOfElementsIn(array):
#     n=len(array)
#     sum=0
#     for i in array:
#         sum+=i
#     return sum//n

# list=[1,2,3,4,5]
# print(sumOfElementsIn(list))


# # reverse an array
# def quickSort(arr):
#     if len(arr)<=1:
#         return arr
#     sorted_arr=[]
#     pivot=arr[0]
#     left= [x for x in arr[1:] if x<=pivot]
#     right=[x for x in arr[1:] if x>pivot]
#     return quickSort(left)+[pivot]+quickSort(right)

# arr=[1,2,3,4,5]
# arr=quickSort(arr)

# print(arr[::-1])

# #remove duplicates
# def quickSort(arr):
#     if len(arr)<=1:
#         return arr
#     sorted_arr=[]
#     pivot=arr[0]
#     left= [x for x in arr[1:] if x<=pivot]
#     right=[x for x in arr[1:] if x>pivot]
#     return quickSort(left)+[pivot]+quickSort(right)

# def removeDuplicates(arr):
#     i=1
#     # n=len(arr)
#     while i<len(arr)-1:
#         if arr[i-1]==arr[i]:
#             arr.pop(i-1)
#         else:
#             i+=1
#     return arr
# arr=[1, 2, 5, 8, 6, 8, 9, 11, 1]
# sorted=quickSort(arr)
# print(removeDuplicates(sorted))

# def quickSort(arr):
#     if len(arr)<=1:
#         return arr
#     sorted_arr=[]
#     pivot=arr[0]
#     left= [x for x in arr[1:] if x<=pivot]
#     right=[x for x in arr[1:] if x>pivot]
#     return quickSort(left)+[pivot]+quickSort(right)


# Find missing number (array)
# def sumOfGivenArray(arr):
#     sum=0
#     for i in arr:
#         sum+=i
#     return sum  #   O(n)

# def actualSum(arr):
#     n=arr[-1]#because one element is missing from the array, length of the actual array = length + 1
#     return n*(n+1)//2 # O(1)

# arr=[0,1,2,4,5]
# print(actualSum(arr)-sumOfGivenArray(arr))# total time complexity = O(n)

#missing number in a given range
# def missingNumberInARange(arr):#needs a sorted array
#     a=arr[0]
#     #N= missing element
#     d= 1
#     n= len(arr)

#     #formula: N= a+(n-1)d

#     #find N
#     i=1
#     while i<n:
#         if arr[i]-arr[i-1]!=d:
#             N=(arr[i]-arr[i-1])/2
#         i+=1
        
#     return a+(n-1)*d

# array=[10,11,12,13,15]
# print(missingNumberInARange(array))

# good logic
# def missingNumberInARange(arr):#needs a sorted array

#     n= len(arr)
#     for i in range(1,n):
#         if arr[i]-arr[i-1]!=1:
#             return arr[i-1] + 1

# array=[10,11,13,12,15]
# print(missingNumberInARange(array))


# linear search
# def linearSearch(arr,n):
#     l=len(arr)
#     for i in range(0, l):
#         if arr[i]==n:
#             print(f"{n} found at index {i} ")
#     return arr


# arr=[2, 3, 6, 8, 5]
# n=8
# linearSearch(arr, n)    


# # reverse a string recursively
# def revString(word):

#     l=len(word)
#     if l>0:
#         return
    
# word=input("Enter a string: ")
# revString(word)

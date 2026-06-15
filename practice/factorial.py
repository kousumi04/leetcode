# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))
# output: 120

# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=' ')
#         temp=a
#         a=b+a
#         b=temp
# fibonacci(5)

#output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# list comprehension
animals=['lion', 'tiger', 'monkey', 'elephant', 'frog']
filtered_animal=[animal.title() for animal in animals]
print(filtered_animal)
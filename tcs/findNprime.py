# def sieve(n):
#     prime = [True] * (n + 1)
#     prime[0] = prime[1] = False

#     for i in range(2, int(n**0.5) + 1):
#         if prime[i]:
#             for j in range(i * i, n + 1, i):
#                 prime[j] = False

#     return [i for i in range(2, n + 1) if prime[i]]

# print(sieve(20))



def sieve(n):
    a = list(range(n + 1))
    
    a[0] = 0
    a[1] = 0

    for i in range(2, n + 1):
        if a[i] != 0:
            for j in range(i * 2, n + 1, i):
                a[j] = 0

    for i in a:
        if i != 0:
            print(i)

sieve(7)
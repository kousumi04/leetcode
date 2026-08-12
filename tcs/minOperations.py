p, q, r = map(int, input().split())

if p == q and q == r:
    print(0)
else:
    arr = [p, q, r]
    arr.sort()

    step = 0

    while True:
        arr[0] += 1
        arr[1] += 1
        arr[2] -= 1
        step += 1

        if arr[0] == arr[1] and arr[1] == arr[2]:
            print(step)
            break

        arr.sort()

        if ((arr[0] - arr[1] == 1 and arr[1] + 1 == arr[2]) or
            (arr[1] - arr[2] == 1 and arr[0] + 1 == arr[1])):
            print(-1)
            break
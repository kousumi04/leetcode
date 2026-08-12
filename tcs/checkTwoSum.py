nums = list(map(int, input().split()))
target = int(input())

seen = {}
found = False

for i in range(len(nums)):
    complement = target - nums[i]

    if complement in seen:
        print("Yes")
        found = True
        break

    seen[nums[i]] = i

if found == False:
    print("No")
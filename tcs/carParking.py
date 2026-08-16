rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
max_ones = 0
ans = 0
for i in range(rows):
    count = 0
    for j in range(cols):
        if matrix[i][j] == 1:
            count += 1
    if count > max_ones:
        max_ones = count
        ans = i + 1
print(ans)
a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))

r = [[0 for i in range(b)] for j in range(a)]
r[0][0] = 1

for i in range(a):
    if r[i][j] == 0:
        continue
    for j in range(1, b):
        if l[i][j] < l[i][j - 1]:
            r[i][j] += r[i][j - 1]
    for j in range(b - 2, -1, -1):
        if l[i][j] < l[i][j + 1]:
            r[i][j] += r[i][j + 1]
    if i == a-1:
        break
    for j in range(b):
        if l[i][j] > l[i + 1][j]:
            r[i + 1][j] += r[i][j]

print(r[-1][-1])
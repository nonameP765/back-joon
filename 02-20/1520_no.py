a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))

r = [[0 for i in range(b)] for j in range(a)]
r[-1][-1] = 1

for i in range(a-1, -1, -1):

    for j in range(b - 1, -1, -1):
        for k in r:
            print(k)
        print()
        if not j == 0 and l[i][j] < l[i][j - 1]:
            r[i][j - 1] += r[i][j]
        if not j == b - 1 and l[i][j] < l[i][j + 1]:
            r[i][j + 1] += r[i][j]
        if not i == 0 and r[i][j] < l[i - 1][j]:
            r[i - 1][j] += r[i][j]

print(r)
print(r[-1][-1])
l = list()
r = list()
c = int(input())

for i in range(c):
    l.append(list(map(int, input().split(' '))))

r.append(l[0])

for i in range(1, c):
    tmp = [l[i][0] + r[i - 1][0]]
    for j in range(1, len(l[i]) - 1):
        tmp.append((r[i - 1][j - 1] if r[i - 1][j] < r[i - 1][j - 1] else r[i - 1][j]) + l[i][j])
    tmp.append(l[i][-1] + r[i - 1][-1])
    r.append(tmp)

print(max(r[-1]))

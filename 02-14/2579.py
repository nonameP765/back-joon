c = int(input())
l = list()

for i in range(c):
    l.insert(0, int(input()))

r = [[0, l[0], 0]]

for i in range(1, c):
    if i == 1:
        r.append([r[0][1], 0, r[0][1] + l[1]])
    elif i == 2:
        r.append([r[1][2], r[1][0] + l[2], 0])
    elif i == 3:
        r.append([r[2][1], r[2][0] + l[3], r[2][1] + l[3]])
    else:
        r.append([r[i-1][1] if r[i-1][1] > r[i-1][2] else r[i-1][2],
                  r[i-1][0] + l[i],
                  r[i-1][1] + l[i]])

print(max(r[-1]))

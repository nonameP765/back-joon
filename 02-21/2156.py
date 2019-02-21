l = list()
for i in range(int(input())):
    l.append(int(input()))

r = [(0, l[0], l[0])]

for i in range(1, len(l)):
    r.append((max(r[i - 1]), r[i-1][0] + l[i], r[i-1][1] + l[i]))

print(max(r[-1]))
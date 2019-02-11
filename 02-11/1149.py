l = list()
l2 = list()
for i in range(int(input())):
    l.append(list(map(int, input().split(' '))))

l2.append(l[0])

for i in range(1, len(l)):
    l2.append(list())
    l2[i].append(l2[i-1][2] + l[i][0] if l2[i-1][1] > l2[i-1][2] else l2[i-1][1] + l[i][0])
    l2[i].append(l2[i - 1][0] + l[i][1] if l2[i - 1][2] > l2[i - 1][0] else l2[i-1][2] + l[i][1])
    l2[i].append(l2[i - 1][1] + l[i][2] if l2[i - 1][0] > l2[i - 1][1] else l2[i-1][0] + l[i][2])


print(min(l2[-1]))
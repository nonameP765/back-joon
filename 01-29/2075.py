n = int(input())
find = list()

for i in input().split(' '):
    i = int(i)
    if len(find) == 0:
        find.append(i)
        continue
    if i > find[0]:
        find.insert(0, i)
    elif find[0] > i > find[-1]:
        for k in range(len(find) - 1):
            if find[k] > i > find[k + 1]:
                find.insert(k + 1, i)
    else:
        find.append(i)

for i in range(n - 1):
    for j in input().split(' '):
        j = int(j)
        if j > find[0]:
            find.insert(0, j)
            find.pop(n)
        elif find[0] > j > find[-1]:
            for k in range(len(find) - 1):
                if find[k] > j > find[k + 1]:
                    find.insert(k + 1, j)
                    find.pop(n)

print(find[-1])

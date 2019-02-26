c = int(input())
l = list(map(int, input().split(' ')))

lis = [0, l[0]]

for i in range(1, c):
    if l[i] > lis[-1]:
        lis.append(l[i])
    else:
        for j in range(len(lis) - 1, -1, -1):
            if l[i] < lis[j]:
                continue
            if l[i] > lis[j]:
                lis[j + 1] = l[i]
                break

print(len(lis) - 1)

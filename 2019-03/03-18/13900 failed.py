N = int(input())

li = list(map(int,input().split(' ')))

r = 0

for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        r += li[i] * li[j]

print(r)
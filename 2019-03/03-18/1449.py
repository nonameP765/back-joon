N, L = map(int, input().split(' '))
li = list(map(int, input().split(' ')))

li.sort()

re = 0
i = 0
while i < N:
    for j in range(i + 1, N):
        if li[i] + L - 1 < li[j]:
            re += 1
            i = j - 1
            break
        if j == N - 1:
            i = j
    else:
        re += 1

    i += 1

print(re)

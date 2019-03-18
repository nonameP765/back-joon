N = int(input())


li = list(map(int, input().split(' ')))

visited = [False for i in range(N)]

re = 0

for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if li[i] + 1 == li[j] and not visited[j]:
            visited[j] = True
            break
    else:
        re += 1


print(re)

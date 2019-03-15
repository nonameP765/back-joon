c = int(input())

graph = [list(map(int, input().split(' '))) for _ in range(c)]

# 플로이드 워셜 알고리즘이라 쓰고 3중 반복문이라 읽는다
for k in range(c):
    for i in range(c):
        for j in range(c):
            graph[i][j] = 1 if graph[i][j] == 1 or graph[i][k] == graph[k][j] == 1 else 0

for i in range(c):
    for j in range(c):
        print(graph[i][j], end=' ')
    print()
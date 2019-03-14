N, E = map(int, input().split(' '))

graph = {i: dict() for i in range(1, N + 1)}

for i in range(E):
    a, b, c = map(int, input().split(' '))
    if graph[i].get(

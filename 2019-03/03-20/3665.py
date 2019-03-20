for _ in range(int(input())):
    N = int(input())
    st = list(map(int, input().split(' ')))
    N1 = int(input())
    graph = {st[i]: st[:i] for i in range(N)}

    for i in range(N1):
        a, b = map(int, input().split(' '))
        if b in graph[a]:
            graph[a].remove(b)
        else:
            graph[a].append(b)
        if a in graph[b]:
            graph[b].remove(a)
        else:
            graph[b].append(a)

    print(graph)

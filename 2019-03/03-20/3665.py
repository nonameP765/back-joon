for _ in range(int(input())):
    N = int(input())
    st = list(map(int, input().split(' ')))
    N1 = int(input())
    graph = {i: {j: False for j in range(1, N + 1)} for i in range(1, N + 1)}
    count = {i: 0 for i in range(1, N + 1)}
    for i in range(N):
        for j in st[i + 1:]:
            graph[st[i]][j] = True
            count[j] += 1

    for i in range(N1):
        a, b = map(int, input().split(' '))
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            count[a] += 1
            count[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            count[b] += 1
            count[a] -= 1

    is_start = False
    is_double = False
    for i in range(1, N + 1):
        if not is_start and count[i] == 0:
            is_start = True
            start = i
        elif is_start and count[i] == 0:
            is_double = True
            break
    if is_double:
        print('?')
    elif is_start:
        result = list()
        queue = list()
        queue.append(start)

        for i in range(1, N + 1):
            if not queue:
                print('IMPOSSIBLE')
                break
            now = queue.pop(0)
            result.append(now)
            for nxt in range(1, N + 1):
                if graph[now][nxt]:
                    count[nxt] -= 1
                    if count[nxt] == 0:
                        queue.append(nxt)
        else:
            for i in result:
                print(i, end=' ')
            print()

    else:
        print('IMPOSSIBLE')

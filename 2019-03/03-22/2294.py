n, k = map(int, input().split())
li = [int(input()) for i in range(n)]


INF = 1e9

li.sort()

re = INF

stack = list()

stack.append((k, 0))

check = [INF for _ in range(k + 1)]

while stack:
    now, w = stack.pop()
    if check[now] < w:
        continue
    for i in li:
        for j in range(now // i + 1):
            nxt_n = now - i * j
            nxt_w = w + j
            if check[nxt_n] > nxt_w:
                stack.append((nxt_n, nxt_w))
                check[nxt_n] = nxt_w
r = check[0]
if r == INF:
    print(-1)
else:
    print(r)
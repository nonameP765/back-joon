a, b = map(int, input().split(' '))
l = list(map(int, input().split(' ')))

c = 0


def dfs(now, index):
    global c
    if index == a:
        return
    if now + l[index] == b:
        c += 1

    dfs(now + l[index], index + 1)
    dfs(now, index + 1)


dfs(0, 0)

print(c)

def dfs(lis, index):
    if 6 - len(lis) > len(a) - index:
        return
    if len(lis) == 6:
        print(' '.join(lis))
        return

    tmp = lis[:]
    tmp.append(a[index])
    dfs(tmp, index + 1)
    dfs(lis, index + 1)


while True:
    a = input().split(' ')
    if a[0] == '0':
        break
    dfs([], 1)
    print()

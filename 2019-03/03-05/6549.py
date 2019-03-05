while True:
    l = list(map(int, input().split(' ')))
    n = l[0]
    if n == 0:
        break
    l = l[1:]
    mx = 0
    for i in range(n):
        tmp = 0

        for j in range(i - 1, -1, -1):
            if l[i] > l[j]:
                break
            tmp += 1
        for j in range(i, n):
            if l[i] > l[j]:
                break
            tmp += 1
        mx = max(mx, tmp * l[i])

    print(mx)

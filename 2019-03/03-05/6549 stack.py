while True:
    l = list(map(int, input().split(' ')))
    n = l[0]
    if n == 0:
        break
    l = l[1:]
    mx = 0
    stack = [0]
    for i in range(1, n):
        while len(stack) != 0 and l[stack[-1]] > l[i]:
            tmp = stack.pop()
            if len(stack) != 0:
                w = i - stack[-1] - 1
            else:
                w = i
            mx = max(mx, l[tmp] * w)
        stack.append(i)

    while len(stack) != 0:
        tmp = stack.pop()
        if len(stack) != 0:
            w = n - stack[-1] - 1
        else:
            w = n
        mx = max(mx, l[tmp] * w)

    print(mx)

for i in range(int(input())):
    a, b = map(int, input().split(' '))
    q = [i for i in range(a)]
    r = list(map(int, input().split(' ')))

    n = 0
    while True:
        if max(r) == r[0]:
            n += 1
            r.pop(0)
            if b == q.pop(0):
                print(n)
                break
        else:
            r.append(r.pop(0))
            q.append(q.pop(0))



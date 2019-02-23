for i in range(int(input())):
    _a, _b = map(int, input().split(' '))

    a, b = (_a, _b) if _a > _b else (_b, _a)

    mi = b

    while a % b != 0:
        tmp = b
        b = a % b
        a = tmp
    else:
        mi = b

    print((_a // mi) * _b)



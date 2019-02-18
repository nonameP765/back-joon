c = input()
a = list(map(int, input().split(' ')))

if c == '1':
    print(a[0])
else:
    mx = a[0] + a[1]
    n = 0
    for i in a:
        n += i
        mx = mx if mx > n else n
        if n < 0:
            n = 0

    print(mx)
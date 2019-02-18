c = input()
a = list(map(int, input().split(' ')))

# 이거때문에 런타임에러로 고생
if c == '1':
    print(a[0])
else:
    # 최고 수
    mx = a[0] + a[1]
    # 현재 합
    n = 0
    for i in a:
        n += i
        mx = mx if mx > n else n
        # 만약 합이 0아래면 다음부터 다시 합함
        if n < 0:
            n = 0

    print(mx)

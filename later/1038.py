c = int(input())

count = 0
num = 1

if 1023 <= c:
    print(-1)
else:

    while True:
        is_down = True
        now = num

        while now >= 10:
            if not now % 10 < now // 10 % 10:
                is_down = False
            if not is_down:
                break
            now //= 10
        if is_down:
            count += 1
            if count == c:
                print(num)
                break
        print(num)


c = int(input())

if c < 10:
    print(c)
elif 1023 <= c:
    print(-1)
else:
    count = 9
    num = 10
    w = [10 ** i for i in range(10)]
    while True:
        now = num
        first = now % 10

        digit = 0
        while True:
            if now % 10 != first + digit:
                break
            digit += 1
            now //= 10
        count += 1
        if count == c:
            print(num)
            break
        if digit <= 1:
            num += 1
        else:
            if num // w[digit - 1] == 9:
                num = 0
                for i in range(digit + 1):
                    num += i * (10 ** i)
            else:
                num = num + w[digit - 1] - num % w[digit - 1]
                for i in range(digit - 1):
                    num += i * (10 ** i)

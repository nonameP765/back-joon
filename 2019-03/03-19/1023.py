N, K = map(int, input().split(' '))


def is_gaul(st):
    stack = list()

    for i in st:
        if i == '0':
            stack.append(i)
        elif i == '1':
            if len(stack) != 0:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True


c = 0
i = 0
while True:
    b = str(bin(i))[2:]
    if len(b) < N:
        b = '0' * (N - len(b)) + b
    if len(b) > N:
        print(-1)
        break
    if not is_gaul(b):
        if c == K:
            for i in b:
                if i == '0':
                    print('(', end='')
                if i == '1':
                    print(')', end='')
            break
        c += 1
    i += 1

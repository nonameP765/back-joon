# 계산한거 저장
zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(p0):
    l = len(zero)
    if l <= p0:
        for i in range(l, p0 + 1):
            zero.append(one[i - 1])
            one.append(one[i - 1] + zero[i - 1])
    print(f'{zero[p0]} {one[p0]}')


for i in range(int(input())):
    fibo(int(input()))

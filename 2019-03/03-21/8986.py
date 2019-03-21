N = int(input())

li = list(map(int, input().split()))

left = 1

right = int(1e9)

re = int(1e18)

while right - left > 2:
    pos1 = (left * 2 + right) // 3
    pos2 = (left + right * 2) // 3

    tmp1 = 0
    tmp2 = 0
    for i in range(N):
        tmp1 += abs(li[i] - (li[0] + pos1 * i))
        tmp2 += abs(li[i] - (li[0] + pos2 * i))
    re = min(re, tmp1, tmp2)
    if tmp1 == tmp2:
        left = pos1
        right = pos2
    elif tmp1 > tmp2:
        left = pos1 + 1
    else:
        right = pos2
    # print()

print(re)
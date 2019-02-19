a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))


def s(i, j):
    if i == a-1 and j == b-1:
        return 1
    re = 0
    if i < a - 1 and l[i][j] > l[i + 1][j]:
        re += s(i + 1, j)
    if j > 0 and l[i][j] > l[i][j - 1]:
        re += s(i, j - 1)
    if j < b - 1 and l[i][j] > l[i][j + 1]:
        re += s(i, j + 1)

    return re


print(s(0, 0))

a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))

success = [[0 for i in range(b)] for j in range(a)]
success[-1][-1] = 1


def s(i, j):
    if success[i][j] == 1:
        return 1
    if i == a - 1 and j == b - 1:
        return 1
    re = 0
    if j > 0 and l[i][j] > l[i][j - 1]:
        re += s(i, j - 1)
    if j < b - 1 and l[i][j] > l[i][j + 1]:
        re += s(i, j + 1)
    if i < a - 1 and l[i][j] > l[i + 1][j]:
        re += s(i + 1, j)
    if re > 0:
        success[i][j] += 1
    return re


print(s(0, 0))
print(success)

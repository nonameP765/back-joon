a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))

success = [[-1 for i in range(b)] for j in range(a)]
success[-1][-1] = 1


def s(i, j):
    if i == a - 1 and j == b - 1:
        return
    if success[i][j] == -1:
        if j < b - 1 and l[i][j] > l[i][j + 1]:
            s(i, j + 1)
            success[i][j] += success[i][j + 1] + 1
        if i < a - 1 and l[i][j] > l[i + 1][j]:
            s(i + 1, j)
            success[i][j] += success[i + 1][j] + 1
        if i > 0 and l[i][j] > l[i - 1][j]:
            s(i - 1, j)
            success[i][j] += success[i - 1][j] + 1
        if j > 0 and l[i][j] > l[i][j - 1]:
            s(i, j - 1)
            success[i][j] += success[i][j - 1] + 1


s(0, 0)
print(success)
print(success[0][0])

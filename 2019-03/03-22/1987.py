R, C = map(int, input().split(' '))

ma = list()

for _ in range(R):
    ma.append(list(input()))

visited = dict()

# for i in ma:
#     for j in i:
#         visited[j] = False

stack = list()
stack.append(((0, 0), {ma[0][0]}, 1))

result = 0
while stack:
    (i, j), his, w = stack.pop()
    result = max(result, w)

    if i > 0:
        if not ma[i - 1][j] in his:
            tmp = his.copy()
            tmp.add(ma[i - 1][j])
            stack.append(((i - 1, j), tmp, w + 1))
    if j > 0:
        if not ma[i][j - 1] in his:
            tmp = his.copy()
            tmp.add(ma[i][j - 1])
            stack.append(((i, j - 1), tmp, w + 1))
    if i < R - 1:
        if not ma[i + 1][j] in his:
            tmp = his.copy()
            tmp.add(ma[i + 1][j])
            stack.append(((i + 1, j), tmp, w + 1))
    if j < C - 1:
        if not ma[i][j + 1] in his:
            tmp = his.copy()
            tmp.add(ma[i][j + 1])
            stack.append(((i, j + 1), tmp, w + 1))

print(result)

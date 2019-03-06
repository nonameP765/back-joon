c = int(input())
l = [list(map(int, input())) for i in range(c)]

visited = [[False for j in range(c)] for i in range(c)]


count = 0
result = list()
for i in range(c):
    for j in range(c):
        if not visited[j][i] and l[j][i] == 1:
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                if not visited[b][a]:
                    if l[b][a] == 0:
                        if count != 0:
                            result.append(count)
                            count = 0

                    if l[b][a] == 1:
                        count += 1
                        if 0 < a and l[b][a - 1] == 1:
                            stack.append((a - 1, b))
                        if 0 < b and l[b - 1][a] == 1:
                            stack.append((a, b - 1))
                        if a < c - 1 and l[b][a + 1] == 1:
                            stack.append((a + 1, b))
                        if b < c - 1 and l[b + 1][a] == 1:
                            stack.append((a, b + 1))
                    visited[b][a] = True
                if len(stack) == 0:
                    if count != 0:
                        result.append(count)
                        count = 0
            visited[j][i] = True



result.sort()
print(len(result))
for i in result:
    print(i)

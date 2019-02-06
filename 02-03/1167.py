c = int(input())

graph = dict()

# 입력
for i in range(c):
    graph[i + 1] = {}

for i in range(c):
    input_list = list(map(int, input().split(' ')))
    for j in range(1, len(input_list) - 1, 2):
        graph[input_list[0]][input_list[j]] = input_list[j + 1]

# 첫번째 dfs
to_visit = [(1, 0)]
visited = [False for i in range(c)]
visited[0] = True
max_length = 0
max_node = 1

while to_visit:
    now, length = to_visit.pop()
    max_length, max_node = (length, now) if length > max_length else (max_length, max_node)
    for i in graph[now].keys():
        if not visited[i - 1]:
            visited[i - 1] = True
            to_visit.append((i, length + graph[now][i]))

# 두번째 dfs
to_visit = [(max_node, 0)]
visited = [False for i in range(c)]
visited[max_node-1] = True
max_length = 0

while to_visit:
    now, length = to_visit.pop()
    max_length = length if length > max_length else max_length

    for i in graph[now].keys():
        if not visited[i - 1]:
            visited[i - 1] = True
            to_visit.append((i, length + graph[now][i]))

print(max_length)

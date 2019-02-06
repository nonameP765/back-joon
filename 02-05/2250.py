count = 0

c = int(input())

graph = dict()
root = [0 for i in range(c + 1)]


for i in range(c):
    graph[i + 1] = {}

# 입력
for i in range(c):
    now, left, right = list(map(int, input().split(' ')))
    graph[now] = (left, right)
    root[now] += 1
    # 자식한테 카운터 한개씩
    if left != -1:
        root[left] += 1
    if right != -1:
        root[right] += 1

# 루트는 자식한테 주는 카운터가 없으니 카운터가 1이겠죠
for i in range(c):
    if root[i + 1] == 1:
        Root = i + 1

lev = list(0 for i in range(c))
his = list(list() for i in range(c + 1))


# 중위순회 기록
def inorder_traversal(root_node, level):
    global count, max_length, max_level, graph

    if graph[root_node][0] != -1:
        inorder_traversal(graph[root_node][0], level + 1)

    count += 1
    his[level].append(count)

    if graph[root_node][1] != -1:
        inorder_traversal(graph[root_node][1], level + 1)


inorder_traversal(Root, 1)

max_length = 0
max_level = 0
# 기록한거 간단하게 비교
for i in range(1, c + 1):
    if len(his[i]) == 0:
        break
    if his[i][-1] - his[i][0] + 1 > max_length:
        max_level = i
        max_length = his[i][-1] - his[i][0] + 1

print(max_level, max_length)

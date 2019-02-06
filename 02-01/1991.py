RootNode = None


class _Node:
    def __init__(self, p0, p1=None, p2=None):
        self.name = p0
        self.left = p1
        self.right = p2


# 추가
def add(name, left, right):
    global RootNode
    # 루트가 없으면 만들어
    if not RootNode:
        RootNode = _Node(name, None if left == '.' else _Node(left), None if right == '.' else _Node(right))
    # 있으면 찾아서 넣어
    else:
        search(RootNode, name, left, right)


# 탐색
def search(now: _Node, name, left, right):
    # 재귀 끝내는부분
    if not now:
        return
    # 자기위치면 자기 자식 생성
    elif now.name == name:
        now.left = None if left == '.' else _Node(left)
        now.right = None if right == '.' else _Node(right)
    # 자기 위치가 아니면 재귀로 찾아
    else:
        search(now.left, name, left, right)
        search(now.right, name, left, right)


def preorder_traversal(root_node: _Node):
    if not root_node:
        return
    print(root_node.name, end='')
    preorder_traversal(root_node.left)
    preorder_traversal(root_node.right)


def inorder_traversal(root_node: _Node):
    if not root_node:
        return
    inorder_traversal(root_node.left)
    print(root_node.name, end='')
    inorder_traversal(root_node.right)


def postorder_traversal(root_node: _Node):
    if not root_node:
        return
    postorder_traversal(root_node.left)
    postorder_traversal(root_node.right)
    print(root_node.name, end='')


c = int(input())
for i in range(1, c):
    m, l, r = input().split(' ')
    add(m, l, r)

preorder_traversal(RootNode)
print()
inorder_traversal(RootNode)
print()
postorder_traversal(RootNode)

class Node:
    def __init__(self, p0):
        self.num = p0
        self.left = None
        self.right = None


def insert(p0, p1):
    global count
    count += 1
    if p0 < p1.num:
        if not p1.left:
            p1.left = Node(p0)
        else:
            insert(p0, p1.left)
    elif p0 > p1.num:
        if not p1.right:
            p1.right = Node(p0)
        else:
            insert(p0, p1.right)


count = 0
for i in range(int(input())):
    now = int(input())

    if i == 0:
        root = Node(now)
        print(0)
        continue
    insert(now, root)
    print(count)

que = list()


def empty(p0):
    if len(p0) == 0:
        return 1
    return 0


def push(p0, p1):
    p0.append(p1)


def pop(p0):
    if empty(p0) == 1:
        return -1
    return p0.pop(0)


def size(p0):
    return len(p0)


def front(p0):
    if empty(p0) == 1:
        return -1
    return p0[0]


def back(p0):
    if empty(p0) == 1:
        return -1
    return p0[-1]


for i in range(int(input())):
    s = input()
    if s.startswith('push'):
        push(que, int(s.split(' ')[1]))
    elif s == 'pop':
        print(pop(que))
    elif s == 'size':
        print(size(que))
    elif s == 'empty':
        print(empty(que))
    elif s == 'front':
        print(front(que))
    elif s == 'back':
        print(back(que))

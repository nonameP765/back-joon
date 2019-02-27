stack = list()

for i in range(int(input())):
    in_str = input().split(' ')
    if in_str[0] == 'push':
        stack.append(int(in_str[1]))
    if in_str[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if in_str[0] == 'size':
        print(len(stack))
    if in_str[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if in_str[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

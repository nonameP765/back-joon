st = input()

stack = list()


i = 0
result = 0
tmp_result = 1
f = False
before = ''
while i < len(st):
    if st[i] == '(':
        stack.append(2)
    if st[i] == ')':
        if len(stack) == 0:
            f = True
            break
        s = stack.pop()

        if s == 2:
            if before == '(':
                tmp = s
                for z in stack:
                    tmp *= z

                result += tmp
        else:
            f = True
            break

    if st[i] == '[':
        stack.append(3)
    if st[i] == ']':
        if len(stack) == 0:
            f = True
            break
        s = stack.pop()

        if s == 3:
            if before == '[':
                tmp = s
                for z in stack:
                    tmp *= z

                result += tmp
        else:
            f = True
            break
    before = st[i]
    i += 1

if len(stack) != 0 or f:
    print(0)
else:
    print(result)
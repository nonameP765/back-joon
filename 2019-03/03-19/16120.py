s = input()


while True:
    stack = list()
    success = False

    for i in range(len(s) - 1):
        if s[i] == 'A':
            if len(stack) >= 2 and s[i + 1] == 'P':
                success = True
                s = s[:i - 1] + s[i + 2:]
                break
            else:
                stack = list()
        else:
            stack.append(1)

    if success:
        if len(s) == 4:
            if s == 'PPAP':
                print('PPAP')
            else:
                print('NP')
            break
    else:
        print('NP')
        break






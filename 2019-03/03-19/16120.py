s = input()

while True:
    s1 = False
    s2 = 0
    for i in range(len(s) - 3):
        if s[i:i+4] == 'PPAP':
            s1 = True
            s2 = i
            break
    if s1:
        if len(s) == 4:
            print('PPAP')
            break
        else:
            s = s[:s2 + 1] + s[s2 + 4:]
    else:
        print('NP')
        break




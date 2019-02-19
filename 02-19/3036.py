c = int(input())

inp = list(map(int, input().split(' ')))

m = inp[0]

for i in range(1, c):
    a = m
    b = inp[i]
    mi = b

    while a % b != 0:
        tmp = b
        b = a % b
        a = tmp
    else:
        mi = b

    print(str(m // mi)+'/'+str(inp[i]//mi))



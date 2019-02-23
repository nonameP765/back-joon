c = int(input())

inp = list(map(int, input().split(' ')))

m = inp[0]

for i in range(1, c):
    a = m
    b = inp[i]
    mi = b
    # 최대공약수 구하기
    while a % b != 0:
        tmp = b
        b = a % b
        a = tmp
    else:
        mi = b

    # 첫번째 톱니//최대공약수, 구할 톱니//최대공약수
    print(str(m // mi)+'/'+str(inp[i]//mi))



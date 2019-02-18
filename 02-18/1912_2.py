input()
a = list(map(int, input().split(' ')))
his = a
mx = 0
now = 1
while his:
    tmp = list()
    for i in range(len(his) - 1):
        if a[i+now] < 0:
            tmp.append(-1)
        elif his[i] == -1:
            tmp.append(-1)
        else:
            n = his[i] + a[i + now]
            mx = n if n>mx else mx
            tmp.append(n)
    his = tmp
    now += 1

print(mx)

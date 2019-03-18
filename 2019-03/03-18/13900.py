N = int(input())

li = list(map(int,input().split(' ')))

re = 0

s = 0

for i in range(N - 1, 0, -1):
    re += li[i]
    s += re * li[i - 1]

print(s)
log = [1, 1, 1, 2, 2, 3]

for i in range(int(input())):
    n = int(input())
    for j in range(len(log), n+1):
        log.append(log[j-5] + log[j-1])
    print(log[n-1])

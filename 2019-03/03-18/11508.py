from heapq import heappush, heappop

hq = list()
N = int(input())

for _ in range(N):
    heappush(hq, int(input()))

r = 0

hq.sort(reverse=True)

for i in range(1, N + 1):
    if i % 3 == 0:
        continue
    r += hq[i - 1]

print(r)
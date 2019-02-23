# 입력값
l = list()
# 합용
l2 = list()
for i in range(int(input())):
    l.append(list(map(int, input().split(' '))))

# 첫번째 합은 당연히 그대로
l2.append(l[0])

for i in range(1, len(l)):
    l2.append(list())
    # 이웃하지 않은 것들중 2개중 작은것을 더함 그걸 R스타트 G스타트 B스타트 다 나눠서 3갈래로 저장
    l2[i].append(l2[i-1][2] + l[i][0] if l2[i-1][1] > l2[i-1][2] else l2[i-1][1] + l[i][0])
    l2[i].append(l2[i - 1][0] + l[i][1] if l2[i - 1][2] > l2[i - 1][0] else l2[i-1][2] + l[i][1])
    l2[i].append(l2[i - 1][1] + l[i][2] if l2[i - 1][0] > l2[i - 1][1] else l2[i-1][0] + l[i][2])

# 최솟값 뽑기로 간단히 출력
print(min(l2[-1]))
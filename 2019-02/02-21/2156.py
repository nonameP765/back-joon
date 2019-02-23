l = list()
for i in range(int(input())):
    l.append(int(input()))

# dp를 위한 배열
r = [(0, l[0], l[0])]

for i in range(1, len(l)):
    r.append(
        (
            # 0번쨰 마시는 경우는 이번꺼 합 안하고 이전 경우중 가장 큰거로 저장
            max(r[i - 1]),
            # 1번째랑 2번째는 각각 0번쨰랑 1번쨰에서 지금 양 더해서 저장
            r[i-1][0] + l[i],
            r[i-1][1] + l[i]
        )
    )

# 결과
print(max(r[-1]))
c = int(input())
l = list(map(int, input().split(' ')))

# lis 사용
lis = [0, l[0]]

for i in range(1, c):
    # 만약 맨마지막 lis값보다 크면 마지막에 추가
    if l[i] > lis[-1]:
        lis.append(l[i])
    else:
        # 이전 lis를 탐색하며 사이값을 갱신
        for j in range(len(lis) - 1, -1, -1):
            # 만약 탐색중인 것보다 작으면 패스
            if l[i] < lis[j]:
                continue
            # 탐색중인 것보다 크면 그 다음걸 체인지
            if l[i] > lis[j]:
                lis[j + 1] = l[i]
                break

print(len(lis) - 1)

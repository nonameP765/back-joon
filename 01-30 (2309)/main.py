input_list = list()
sum = 0  # 모든 난장이의 키를 합함
for i in range(9):
    input_list.append(int(input()))
    sum += input_list[i]
end = False
for i in range(9):
    now = sum - input_list[i]
    for j in range(i + 1, 9):
        # 두명의 난쟁이의 키를 합에서 뺴서 100이 된다면 결과
        if now - input_list[j] == 100:
            input_list.pop(j)
            input_list.pop(i)
            end = True
            break
    if end:
        break


# 병합정렬
def mergeSort(li):
    if len(li) <= 1:
        return li

    m = len(li) // 2  # 중간 기점
    l = li[:m]  # 중간을 기준으로 왼쪽
    r = li[m:]  # 중간을 기준으로 오른쪽

    # 양쪽으로 트리 생성
    lr = mergeSort(l)
    rr = mergeSort(r)

    i = j = 0
    re = list()

    # 트리끼리 순서에 맞게  정렬
    while i < len(lr) and j < len(rr):
        if lr[i] < rr[j]:
            re.append(lr[i])
            i += 1
        elif lr[i] > rr[j]:
            re.append(rr[j])
            j += 1
    else:
        re += lr[i:]
        re += rr[j:]
    return re


input_list = mergeSort(input_list)
for item in input_list:
    print(item)

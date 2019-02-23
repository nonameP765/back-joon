input_list = list()

for i in range(int(input())):
    input_list.append(input().split(' '))

for i in range(len(input_list)):
    count = 1
    for j in range(len(input_list)):
        if i == j:
            continue
        if input_list[i][0] < input_list[j][0] and input_list[i][1] < input_list[j][1]:
            count += 1

    print(count)

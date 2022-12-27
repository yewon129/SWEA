T = int(input())

for tc in range(1, T+1):
    lst = list(map(str, input()))
    flag = 0
    while 1:
        if len(lst) == 1:
            flag = 1
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                lst.pop(i+1)
                lst.pop(i)
                break
            if i == len(lst)-2:
                flag = 1
        if flag == 1:
            break

    print(f"#{tc} {len(lst)}")

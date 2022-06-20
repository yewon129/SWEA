T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    maxV = arr[0]
    for i in range(10):
        if maxV < arr[i]:
            maxV = arr[i]

    print(f'#{tc} {maxV}')
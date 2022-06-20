T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)

    total = 0
    for i in range(N):
        if arr[i] % 2 == 1:
            total += arr[i]

    print(f'#{tc} {total}')
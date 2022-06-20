T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    minV = 100000
    for n in arr:
        if abs(n) < minV:
            minV = abs(n)
            cnt = 1
        elif abs(n) == minV:
            cnt += 1

    print(f'#{tc} {minV} {cnt}')
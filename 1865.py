def f(i,N,s):
    global maxV
    if i == N:
        if maxV < s*100:
            maxV = s*100
    if s * 100 <= maxV:
        return
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                f(i+1, N, s * (arr[i][j] *0.01) )
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    maxV = 0
    p = [0]*N
    f(0, N, 1)
    print(f'#{tc} {format(maxV,".6f")}')

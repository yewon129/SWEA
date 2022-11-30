T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split())) + [N]

    k = K
    cnt = 0
    ans = 1000
    for i in range(1, N):
        k -= 1
        for j in range(M):
            if lst[j+1]-lst[j] > K:
                ans = 0
                break
            if i == lst[j] and lst[j+1]-lst[j] > k:
                k = K
                cnt += 1

    if ans == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {cnt}')
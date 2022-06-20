T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ranks = {1:'A+', 2:'A0', 3:'A-', 4:'B+', 5:'B0', 6:'B-', 7:'C+', 8:'C0', 9:'C-', 10:'D0'}
    scores = [0] * N
    for i in range(N):
        scores[i] += arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.2

    number = scores[K-1]
    scores.sort(reverse=True)

    k = scores.index(number)


    print(f'#{tc} {ranks[k//(N/10)+1]}')
T = int(input())

for _ in range(1, T+1):
    tc = int(input())
    arr = list(map(int, input().split()))
    scores = [0] * 101

    for student in arr:
        scores[student] += 1

    maxV = 0
    maxscore = 0
    for i in range(101):
        if scores[i] >= maxV:
            maxV = scores[i]
            maxscore = i

    print(f'#{tc} {maxscore}')
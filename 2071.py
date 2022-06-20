T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    total = 0
    for i in range(10):
        total += arr[i]

    answer = round(total/10)
    print(f'#{tc} {answer}')
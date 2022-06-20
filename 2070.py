T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    if n > m:
        print(f'#{tc} >')
    elif n < m:
        print(f'#{tc} <')
    else:
        print(f'#{tc} =')
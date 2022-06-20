T = int(input())

for tc in range(1, T+1):
    number = list(map(int, input()))

    year = 1000 * number[0] + 100 * number[1] + 10 * number[2] + number[3]
    month = 10 * number[4] + number[5]
    day = 10 * number[6] + number[7]
    answer = 0

    if month > 12 or month < 1:
        answer = -1

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31 or day <= 0:
            answer = -1

    if month in [4, 6, 9, 11]:
        if day > 30 or day <= 0:
            answer = -1

    if month == 2:
        if day > 28 or day <= 0:
            answer = -1

    if answer == -1:
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} {number[0]}{number[1]}{number[2]}{number[3]}/{number[4]}{number[5]}/{number[6]}{number[7]}')
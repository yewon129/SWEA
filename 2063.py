N = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = arr[N//2]
print(answer)
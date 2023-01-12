T = int(input())
for tc in range(1, T+1):
  N, M = map(int, input().split())
  lst = list(map(int, input().split()))

  minV = 10000000
  maxV = 0

  for i in range(N-M+1):
    cnt = 0
    for j in range(M):
      cnt += lst[i+j]
    if cnt > maxV:
      maxV = cnt
    if cnt < minV:
      minV = cnt
  
  print(f'#{tc} {maxV-minV}')

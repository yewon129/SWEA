def findst(N):
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 2:
        return i, j

def maze(i, j, N):
  v = [[0]*N for _ in range(N)]
  v[i][j] = 1
  while stack:
    i, j = stack.pop()
    if arr[i][j] == 3:
      return 1
    for di, dj in [(1,0), (0,1), (-1, 0), (0,-1)]:
      ni, nj = i+di, j+dj
      if 0<=ni<N and 0<=nj<N and v[ni][nj] != 1 and arr[ni][nj] != 1:
        stack.append((ni,nj))
        v[ni][nj] = 1
  return 0

T = int(input())
for tc in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input())) for _ in range(N)]
  sti, stj = findst(N)
  stack = [(sti, stj)]
  ans = maze(sti, stj, N)
  print(f'#{tc} {ans}')

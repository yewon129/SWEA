def findst():
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 2:
        return i, j

def bfs(i, j):
  q = [(i,j)]
  v = [[0]*N for _ in range(N)]
  while q:
    i,j = q.pop(0)
    if arr[i][j] == 3:
      return v[i][j]-1
    for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
      ni, nj = i+di, j+dj
      if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and v[ni][nj] == 0:
        q.append((ni,nj))
        v[ni][nj] = v[i][j] + 1
  return 0

T = int(input())

for tc in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input())) for _ in range(N)]
  sti, stj = findst()
  ans = bfs(sti,stj)

  print(f'#{tc} {ans}')

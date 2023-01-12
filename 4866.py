T = int(input())
for tc in range(1, T+1):
  lst = map(str, input())
  stack = []
  flag = 1

  for s in lst:
    if s == '{':
      stack.append('{')
    elif s == '}':
      if len(stack) != 0 and stack[-1] == '{':
        stack.pop()
      else:
        flag = 0
    elif s == '(':
      stack.append('(')
    elif s == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      else:
        flag = 0
    if flag == 0:
      break
  if len(stack) != 0:
    flag = 0

  print(f'#{tc} {flag}')

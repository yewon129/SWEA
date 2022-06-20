arr = list(map(str, input()))

for c in arr:
    print(f'{ord(c) - 64}', end=' ')
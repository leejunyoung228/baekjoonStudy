h, m = map(int, input().split())
if m >= 45:
    m -= 45
else:
    if h > 0:
        h -= 1
        m += 15
    else:
        h = 23
        m += 15
print(f'{h} {m}')
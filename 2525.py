h, m = map(int, input().split())
t = int(input())
if m + t >= 60:
    h += (m + t) // 60
    m = (m + t)%60
    h %= 24
else:
    m += t
print(f'{h} {m}')
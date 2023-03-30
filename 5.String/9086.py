t = int(input())
s = []
for _ in range(t):
    s.append(input())
for i in s:
    print(f'{i[0]}{i[-1]}')
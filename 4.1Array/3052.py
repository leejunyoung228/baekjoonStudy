l = []
for _ in range(10):
    l.append(int(input())%42)
l = set(l)
print(len(l))
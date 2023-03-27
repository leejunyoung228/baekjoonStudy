c = [i for i in range(1,31)]
for i in range(28):
    c.remove(int(input()))
print(f'{min(c)}\n{max(c)}')
l = list()
for i in range(9):
    l.append(int(input()))
print(f'{max(l)}\n{l.index(max(l))+1}')
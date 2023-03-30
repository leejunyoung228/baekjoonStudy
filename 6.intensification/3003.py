c = [1, 1, 2, 2, 2, 8]
i_c = list(map(int, input().split()))
sub = [c[i] - i_c[i] for i in range(len(c))]
for i in sub:
    print(i, end=" ")
print()
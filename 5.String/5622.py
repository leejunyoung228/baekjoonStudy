S = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
count = 0
for s in S:
    for i in dial:
        if s in i:
            count += dial.index(i) + 3
print(count)
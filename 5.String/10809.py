s = input()
result = [-1] * 26
for i in s:
    result[ord(i)-ord('a')] = s.index(i)
for i in result:
    print(i, end=' ')
print()
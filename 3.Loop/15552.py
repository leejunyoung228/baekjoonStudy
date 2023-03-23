import sys
t = int(input())
testCase = []
result = []
for i in range(t):
    testCase.append(list(map(int, sys.stdin.readline().split())))
for i in testCase:
    result.append(i[0]+i[1])
for i in result:
    print(i)
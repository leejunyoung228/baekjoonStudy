x = int(input())
n = int(input())
l = []
money = 0
for i in range(n):
    l.append(input().split())
for i in l:
    money += int(i[0]) * int(i[1])
if x == money:
    print("Yes")
else:
    print("No")
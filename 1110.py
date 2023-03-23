n = int(input())
count = 0
num = n
while True:
    num = (int(str(num)[0]) + int(str(num)[1]))%10 + (int(str(num)[1]) * 10)
    count += 1
    if num == n:
        print(count)
        break
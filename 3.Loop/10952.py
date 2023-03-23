s=[]
while True:
    a=list(map(int,input().split(" ")))
    if a[0]+a[1]==0:break
    s.append(a[0]+a[1])
for i in s:
    print(i)
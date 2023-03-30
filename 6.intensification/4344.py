c = int(input())
tcl = []
for _ in range(c):
    tcl.append(list(map(int, input().split())))
for tc in tcl:
    avg = sum(tc[1:])/tc[0]
    c = len([i for i in tc[1:] if i > avg])
    print(f'{c/tc[0]*100:.3f}%')
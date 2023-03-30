n = int(input())
array = list(map(float, input().split()))
print(sum([i / max(array) * 100 for i in array]) / n)
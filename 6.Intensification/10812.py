n, m = map(int, input().split())
basket = [i+1 for i in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    basket = basket[:i-1]+basket[k-1:j]+basket[i-1:k-1]+basket[j:]
for b in basket:
    print(b,end=" ")
print()
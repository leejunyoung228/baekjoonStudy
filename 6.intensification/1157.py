word = input().upper()
u_word = list(set(word))
count = []
for w in u_word:
    count.append(word.count(w))
if count.count(max(count)) > 1:
    print("?")
else:
    print(u_word[count.index(max(count))])
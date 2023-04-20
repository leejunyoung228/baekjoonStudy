word = input()
r_word = "".join([i for i in list(word)[::-1]])
if word == r_word:
    print(1)
else:
    print(0)
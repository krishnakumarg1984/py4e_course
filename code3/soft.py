txt = "but soft what light in yonder window breaks"
words = txt.split()
t = []
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = []
for length, word in t:
    res.append(word)

print(res)

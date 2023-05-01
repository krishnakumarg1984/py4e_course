with open("mbox-short.txt", encoding="UTF-8") as fhand:
    for line in fhand:
        line = line.rstrip()
        if not line.startswith("From "):
            continue
        words = line.split()
        print(words[2])

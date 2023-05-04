# Search for lines that start with From and have an at sign
import re

hand = open("mbox-short.txt", encoding="UTF-8")
for line in hand:
    line = line.rstrip()
    if re.search("^From:.+@", line):
        print(line)

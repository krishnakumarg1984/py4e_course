# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
# print(line.rstrip())

# fname = "romeo.txt"
fname = input("Enter file name: ")
unique_words_in_file = []
with open(fname, encoding="UTF-8") as fh:
    for line in fh:
        for word in line.split():
            if word not in unique_words_in_file:
                unique_words_in_file.append(word)

unique_words_in_file.sort()
print(unique_words_in_file)

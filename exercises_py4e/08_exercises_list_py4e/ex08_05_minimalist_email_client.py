fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
mail_count = 0
with open(fname, encoding="UTF-8") as fh:
    for line in fh:
        words = line.split()
        if len(words) == 0 or words[0] != "From":
            continue
        print(words[1])
        mail_count += 1

print(f"There were {mail_count} lines in the file with From as the first word")

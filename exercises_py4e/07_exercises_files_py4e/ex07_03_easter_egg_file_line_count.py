import sys

fname = input("Enter a file name: ")

try:
    fhand = open(fname, encoding="utf-8")
except FileNotFoundError:
    print(f"File cannot be opened: {fname}")
    sys.exit()

easter_egg_string = "na na boo boo"
if fname == easter_egg_string:
    print(f"{fname.upper()} - You have been punk'd!")
else:
    subject_linecount = 0
    for line in fhand:
        if not line.startswith("Subject:"):
            continue
        subject_linecount += 1

    print(f"There were {subject_linecount} subject lines in {fname}")

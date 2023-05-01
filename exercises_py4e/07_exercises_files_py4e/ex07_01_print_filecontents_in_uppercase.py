import sys

fname = input("Enter a file name: ")
try:
    fhand = open(fname, encoding="utf-8")
except:
    print(f"Unable to open file {fname}")
    sys.exit()

for line in fhand:
    print(line.upper())

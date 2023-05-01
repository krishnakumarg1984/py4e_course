import sys

fname = input("Enter file name: ")

try:
    fh = open(fname, encoding="utf-8")
except FileNotFoundError:
    print(f"Unable to open file {fname}")
    sys.exit()


spam_linecount = 0
total_spam_confidence = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    total_spam_confidence += float(line[line.find(":") + 1 :].strip())
    spam_linecount += 1

print(f"Average spam confidence: {total_spam_confidence/spam_linecount}")

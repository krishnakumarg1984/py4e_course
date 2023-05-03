# Exercise 2:
# This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

from typing import Dict

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

hourofday_histogram: Dict[str, int] = {}
try:
    with open(fname, encoding="UTF-8") as fh:
        for line in fh:
            words_in_line = line.split()
            if len(words_in_line) < 6 or words_in_line[0] != "From":
                continue
            hour_of_day = words_in_line[5].split(":")[0]
            hourofday_histogram[hour_of_day] = (
                hourofday_histogram.get(hour_of_day, 0) + 1
            )
except:
    print("Unable to open file", fname)

for hour, count in sorted(hourofday_histogram.items()):
    print(hour, count)

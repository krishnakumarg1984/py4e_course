# Exercise 2:
# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary(order does not matter).

from typing import Dict

# fname = "haha.txt"
fname = input("Enter a file: ")
dow_histogram: Dict[str, int] = {}
try:
    with open(fname, encoding="UTF-8") as fh:
        for line in fh:
            words_in_line = line.split()
            if len(words_in_line) < 3 or words_in_line[0] != "From":
                continue
            dow = words_in_line[2]
            dow_histogram[dow] = dow_histogram.get(dow, 0) + 1

    print(dow_histogram)
except FileNotFoundError:
    print(f"Error! File {fname} not found!")
except PermissionError:
    print(f"Error! Unable to open {fname} due to incorrect permissions")

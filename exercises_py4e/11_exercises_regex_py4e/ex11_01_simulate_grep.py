# Exercise 1:
# Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re

search_pattern = input("Enter a regular expression: ")
fname = "mbox.txt"

result_lines_count = 0
with open(fname, encoding="UTF-8") as fh:
    for line in fh:
        if re.search(search_pattern, line):
            result_lines_count += 1
        # matches_in_line = re.findall(search_pattern, line)
        # if len(matches_in_line) > 0:
        #     result_lines_count += 1
        #     # print(matches_in_line)

print(f"{fname} had {result_lines_count} lines that matched {search_pattern}")

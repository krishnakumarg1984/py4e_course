# Exercise 2:
# Write a program to look for lines of the form:
#
# New Revision: 39772
#
# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the # average as an integer.

import re

search_pattern = "^New Revision: ([0-9]+)$"
fname = input("Enter file: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

revnum_sum = 0
matching_lines_count = 0
with open(fname, encoding="UTF-8") as fh:
    for line in fh:
        revision_number_list = re.findall(search_pattern, line)
        if revision_number_list:
            revnum_sum += int(revision_number_list[0])
            matching_lines_count += 1

print(f"{revnum_sum // matching_lines_count}")

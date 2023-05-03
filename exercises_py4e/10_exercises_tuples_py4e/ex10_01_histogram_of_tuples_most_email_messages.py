# Exercise 1:
# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

from typing import Dict

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

email_histogram: Dict[str, int] = {}
try:
    with open(fname, encoding="UTF-8") as fh:
        for line in fh:
            words_in_line = line.split()
            if len(words_in_line) < 2 or words_in_line[0] != "From:":
                continue
            email_address = words_in_line[1]
            email_histogram[email_address] = email_histogram.get(email_address, 0) + 1

    # print(email_histogram)
except:
    print("Unable to open file", fname)

email_histogram_list = [
    (count, email_id) for (email_id, count) in email_histogram.items()
]
email_histogram_list.sort(reverse=True)
print(email_histogram_list[0][1], email_histogram_list[0][0])

# Exercise 3:
# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

fname = input("Enter file name: ")
email_histogram = {}
try:
    with open(fname, encoding="UTF-8") as fh:
        for line in fh:
            words_in_line = line.split()
            if len(words_in_line) < 2 or words_in_line[0] != "From:":
                continue
            email_address = words_in_line[1]
            email_histogram[email_address] = email_histogram.get(email_address, 0) + 1

    print(email_histogram)
except:
    print("Unable to open file", fname)

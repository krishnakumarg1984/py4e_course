# Exercise 4:
# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

fname = input("Enter a file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
email_histogram = {}
try:
    with open(fname, encoding="UTF-8") as fh:
        for line in fh:
            words_in_line = line.split()
            if len(words_in_line) < 2 or words_in_line[0] != "From:":
                continue
            email_address = words_in_line[1]
            email_histogram[email_address] = email_histogram.get(email_address, 0) + 1

    # print(email_histogram)

    most_email_sender = None
    max_email_count = None
    for sender in email_histogram:
        if max_email_count is None or email_histogram[sender] > max_email_count:
            most_email_sender = sender
            max_email_count = email_histogram[sender]

    print(most_email_sender, max_email_count)
except:
    print("Unable to open file", fname)

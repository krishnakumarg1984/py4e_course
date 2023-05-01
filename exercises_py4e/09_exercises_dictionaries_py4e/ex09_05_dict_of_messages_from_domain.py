# Exercise 5:
# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

fname = input("Enter a file name: ")
domain_histogram = {}
try:
    with open(fname, encoding="UTF-8") as fh:
        for line in fh:
            words_in_line = line.split()
            if len(words_in_line) < 2 or words_in_line[0] != "From:":
                continue
            email_address = words_in_line[1]
            domain_name = email_address.split("@")[1]
            domain_histogram[domain_name] = domain_histogram.get(domain_name, 0) + 1

    print(domain_histogram)

except:
    print("Unable to open file", fname)

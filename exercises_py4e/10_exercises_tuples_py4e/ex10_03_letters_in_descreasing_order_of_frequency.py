# Exercise 3:
# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
from typing import Dict

fname = input("Enter file name: ")
if len(fname) < 1:
    # fname = "romeo.txt"
    # fname = "romeo_mod.txt"
    fname = "romeo.txt"

letter_hist: Dict[str, int] = {}
try:
    with open(fname, encoding="UTF-8") as fh:
        for line in fh:
            line = line.rstrip()
            line = line.translate(
                line.maketrans("", "", string.punctuation + " 0123456789")
            )
            line = line.lower()
            for char in line:
                letter_hist[char] = letter_hist.get(char, 0) + 1

    letter_hist_list = [(v, k) for (k, v) in letter_hist.items()]
    letter_hist_list.sort(reverse=True)
    # print(letter_hist_list)
    for count, letter in letter_hist_list:
        print(letter, count)
except:
    print("Unable to open file", fname)

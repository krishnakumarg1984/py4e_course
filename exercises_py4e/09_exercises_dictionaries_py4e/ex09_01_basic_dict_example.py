# Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

words_dict = {}
with open("words.txt", encoding="UTF-8") as fh:
    for line in fh:
        words_in_line = line.split()
        for word in words_in_line:
            words_dict[word] = "val"

print("hello" in words_dict)
print("in" in words_dict)

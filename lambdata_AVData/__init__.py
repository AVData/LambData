'''
Assignment 1
'''
#
# import pandas as pd
# import numpy as np
#
# ONES = pd.DataFrame(np.ones(10))
# ZEROS = pd.DataFrame(np.zeros(50))

# Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages.  The program looks for "From "
# lines and takes the second word of those lines as the person who sent the
# mail.  The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file.  After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.


NAME = input("Enter file: ")
FHAND = open(NAME)
WORDS = list()
#count = 0

for line in FHAND:
    if not line.startswith("From "):
        continue
    line = line.split()
    WORDS.append(line[1])
#    emails[words] = line[1]

COUNTS = dict()

for word in WORDS:
    COUNTS[word] = COUNTS.get(word, 0) + 1

BIGCOUNTS = None
BIGWORD = None
for email, COUNTS in COUNTS.items():
    if BIGCOUNTS is None or COUNTS > BIGWORD:
        BIGWORD = email
        BIGCOUNTS = COUNTS

print(BIGWORD, BIGCOUNTS)


#    count = count + 1
#    print(words[1])
#print("There were", count, "lines in the file with From as the first word")

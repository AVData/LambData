'''
lambdata - a  collection of data science helper funcitons
'''
#
import pandas as pd
import numpy as np
import sklearn

# Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages.  The program looks for "From "
# lines and takes the second word of those lines as the person who sent the
# mail.  The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file.  After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.


# name = input("Enter file: ")
# fhand = open(name)
# words = list()
# #count = 0
#
# for line in fhand:
#     if not line.startswith("From "): continue
#     line = line.split()
#     words.append(line[1])
# #    emails[words] = line[1]
#
# counts = dict()
#
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
#
# bigcount = None
# bigword = None
# for email,counts in counts.items():
#     if bigcount is None or counts > bigcount:
#         bigword = email
#         bigcount = counts
#
# print(bigword, bigcount)


#    count = count + 1
#    print(words[1])
#print("There were", count, "lines in the file with From as the first word")

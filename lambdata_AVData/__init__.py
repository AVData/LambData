'''
Assignment 1
'''
#
# import pandas as pd
# import numpy as np
#
# ONES = pd.DataFrame(np.ones(10))
# ZEROS = pd.DataFrame(np.zeros(50))


name = input("Enter file: ")
fhand = open(name)
words = list()
#count = 0

for line in fhand:
    if not line.startswith("From "): continue
    line = line.split()
    words.append(line[1])
#    emails[words] = line[1]

counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for email,counts in counts.items():
    if bigcount is None or counts > bigcount:
        bigword = email
        bigcount = counts

print(bigword, bigcount)
#    count = count + 1
#    print(words[1])
#print("There were", count, "lines in the file with From as the first word")














#

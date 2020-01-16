#EXERCISE 9.1
#
#
#
# EXAMPLE 1: The following program is an example from the lecture on how to use the
# count.get("", ) itiration for counting words.
#
#
#counts = dict()
#print("Enter a line of text: ")
#line = input(" ")
#
#words = line.split()
#
#print("Words: ", words)
#
#print("Counting....")
#for word in words:
#    counts[word] = counts.get(word, 0) + 1
#print("Counts", counts)
#
#
# EXAMPLE 2: In this exmaple we are doing a for loop to show that it goes over
# the keys in a dictionary and not the values. {"key" : value}
#
# Note: python can turn dictionaries into lists if you use the list(dict) on a
# dictionary, and it will render the keys only, not the values; if you want the
# to print out the values you can ask do so by uing the print(dict.values())
# method; lastly you can use the print(dict.items()) to print out both the keys
# and the vlues together as a list.  Food for thought, what is a "tuple"?
#
#
#counts = {"chuck" : 1, "fred" : 42, "jan" : 100}
#for key in counts:
#    print(key, counts[key])
#
#
# SOME DOPE SHIT THAT PYTHON DOES, IT CAN ITERATE OVER TWO ITERATION VARIABLES
#
#
# The following is the code used in the last slide of 9.3, which should be
# useful for the next assignment.
#
#
#name = input("Enter file: ")
#handle = open(name)

#counts = dict()
#for line in handle:
#    words = line.split()
#    for word in words:
#        counts[word] = counts.get(word,0) + 1

#bigcount = None
#bigword = None
#for word,count in counts.items():
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count

#print(bigword, bigcount)
#
#
# Assignment 9.4 because i'm already late as fuck for this one.
#
# Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages.  The program looks for "From "
# lines and takes the second word of those lines as the person who sent the
# mail.  The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file.  After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.
#
#
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

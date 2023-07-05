"""
Program: Scrambled-Challenge
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to sort and print the scrambled words in tuples
Revision: First Revision of Scrambled exercises

"""
#Program Announcement
print("\n***Scrambled Exercises***\n")


z = [('v', 'c', 'l', 6, 'r'), ('i', 'a', 'i', 4, 't'),
     ('a', 'f', 'g', 1, 'p'), ('h', 'n', 'r', 3, 's'),
     ('e', 'e', 'a', 7, 'e'), ('c', 'i', 'o', 2, 'a'),
     ('e', 'n', 'l', 5, 'u')]

#Sorting the tuples based on the integer value in each.  Using a lambda construct to provide the sort key.

z.sort(key=lambda a: a[3])

# Using a list comprehension to create a list of characters for each word.
a=[i[0] for i in z]
b=[i[1] for i in z]
c=[i[2] for i in z]
d=[i[4] for i in z]

#Using the join() method to create a string for each of the four words and printing them.
print("The Scrambled words are listed below :\n")
print("".join(a))
print("".join(b))
print("".join(c))
print("".join(d))

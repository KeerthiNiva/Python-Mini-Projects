"""
Program: Double-Scrambled-Challenge
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to rotate,sort and print the scrambled words in lists
Revision: First Revision of Double Scrambled exercises

"""
#Program Announcement
print("\n***Double Scrambled Exercises***\n")


z = [['s', 'a', 3, 't', 'n'],['h', 'b', 'c', 1, 'p'],
     ['h', 'y', 'c', 'k', 5],[4, 'c', 'e', 'i', 'l'],
     ['o', 'a', 'h', 2, 'i']]

# Rotating each list in z so the integer is in the zero position without changing the order of the characters.
for k,l in enumerate(z):
    for i,j in enumerate(l):
        while(type(l[i])==int):
            x=l.pop()
            l.insert(0,x)

#Sorting the lists based on the integer value in each list
z= sorted(z,key = lambda a:a[0])

#Using a list comprehension to create a list of characters for each word and printing it using join method
print("The Scrambled words are listed below :\n")
for i in range(len(z)-1):
    print(''.join([k[i+1] for k in z]))




"""
Program: Super Scrambled
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to rotate, sort and build the scrambled words
Revision: First Revision of super Scrambled

"""
#Program Announcement
print("\n***Super Scrambled Exercises***\n")

mess = [['o', 'c', 'h', 'c', 'a', 64, 'd'],
        ['o', 'o', 91, 'y', 'y', 'e', 'i'],
        ['u', 'r', 'o', 'u', 'y', 46, 'e'],
        ['u', 'y', 'e', 'r', 19, 't', 't'],
        ['a', 'h', 55, 's', 'n', 'i', 's'],
        [27, 'u', 'r', 't', 'r', 'r', 'n'],
        [72, 'a', 'c', 'p', 't', 'g', 'm']]

# Define the rotate function
def rotateForward(z):
    for k,l in enumerate(z):
        for i,j in enumerate(l):
            while(type(l[i])==int):
                    x=l.pop()
                    l.insert(0,x)
    return z
                    

#  Sorting and building to print the words
print("The Scrambled words are listed below :\n")
for i in range(len(mess)-1):
    for j in rotateForward(mess):
        mess.sort(key=lambda x:x[i])
    print(''.join([k[i+1] for k in rotateForward(mess)]))




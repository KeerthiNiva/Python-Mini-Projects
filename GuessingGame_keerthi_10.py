"""
Program: GuessingGame_keerthi_10
Author: keerthi Nivasshini Thangaraj
Progam Description: Program To Guess the Secret Number
Revision: First Revision of the Guessing Game
"""

#importing functions
import math
import random
#Announce the program
print("Guess the Secret Number")
#Getting input for maximum range from the user
nMax=int(input("Enter the maximum number in the range:"))
#Getting the appropriate number of guesses to find the secret number using math function
print("Try to guess the secret number from 1 to",nMax,"(inclusive)")
nGuesses=int(math.log2(nMax)+1)
#Assigning a secret number using Random function
sNum=random.randrange(1,nMax)
#iterating the loop to guess the number within the number of guesses allowed
for i in range (1,nGuesses+1):
 n=int(input("Enter your guess: "))
 if n<sNum:
   print("The secret number is greater than ",n)
   if nGuesses-i==1:
     print("You have ",nGuesses-i,"guess available")
   else:
     print("You have ",nGuesses-i,"guesses available")
 elif n>sNum:
  print("The secret number is less than ",n)
  if nGuesses-i==1:
     print("You have ",nGuesses-i,"guess available")
  else:
     print("You have ",nGuesses-i,"guesses available")
 else:
   print("You guessed right")
   break
else:#Printing the output if all the available guesses are used
  print("The secret number is ",sNum)

'''
Author:Keerthi Nivasshini Thangaraj
FileName:LinearPrediction_keerthi_01.py
Pupose: To print third number in a sequence
Revision:02
'''

#Print statement for getting input from the user
print("Linear prediction:\nPrint third number in a sequence\n")

#Assigning the input values to the variables
first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number:"))

#calculating third number
third_number=second_number+(second_number-first_number)

#print all the numbers in sequence
print("\nThe linear sequence is",first_number,second_number,third_number)

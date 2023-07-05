'''
Author : Keerthi Nivasshini Thangaraj
File Name: SimpleAverage_keerthi_05.py
Purpose: To compute the average of a sequence of input numbers
Revision:
    00: Announce and read the input value in the form of int
    01: By using for loop get sequence of input numbers from the user
    02: Add the number
    03: Find the average
    04: Print the value
'''
print("Program to compute the average")

#Announce and read the input value in the form of int
number=int(input("How many numbers would you like to average?"))

#initialize variable
add=0

#By using for loop get sequence of input numbers from the user and perform addition
for i in range(1,number+1):
    num1=int(input("Enter number "+str(i)+":"))
    add=num1+add

#Calculating the average 
avg=add/number

#Print the output value for user view
print("The average is",avg)

    
        

"""
Program: Average Revisited
Author:Keerthi Nivasshini Thangaraj
Progam Description: Calculating the average from numbers provided
Revision: First Revision of the Average Revisited

"""
#Program Annoucement
print("\n***Program to compute the average of the numbers provided***\n")
#Instructions to users
print("\nEnter each number followed by <enter>.")
print("When you are done, just hit <enter> in response to the prompt.\n")
#Intitalizing the variable count to get the count of numbers user entered
count=0
#Intializing the variable total to sum all the numbers users entered
total=0
#Using "try" before while loop to "pass" the Valueerror caused when user hit enter in prompt
try:
    while no    :=float(input("Enter a Number: ")):
        count+=1
        total+=no
except ValueError:
    pass
#Printing the output using f string to have .1 decimal and printing the count of numbers user entered
print(f"\nYou entered {count} numbers.")
print(f"The Average is {total/count:.1f}.")

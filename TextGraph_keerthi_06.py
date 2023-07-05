'''
Author : Keerthi Nivasshini Thangaraj
File Name: TextGraph_keerthi_06.py
Purpose: Compute bar graph using characters printed in the console window
Revision:
    00: Announce and read the values.
    01: Use split function to split the value.
    02: Use for loop to run the function upto 5 times.
    03: if() to check the constrains.
    04: Print the value.
'''

print("Textgraph: Draw a bar graph using text")

#Announce and read the input value from the user
response=input("Enter up to 5 positive integers less than 50:")

#Using split function to split the values
number=response.split()

#Considering only first five numbers
number=number[0:5]

#Use for loop to run the function upto 5 times and if loop to check given constraints
n=0
for n in number:
    if n.isnumeric() and int(n)<=50:
        bar=int(n)*'='
        print(bar)
    if (n.isnumeric()==False and type(n)==str) or int(n)>50 :
        print("?")

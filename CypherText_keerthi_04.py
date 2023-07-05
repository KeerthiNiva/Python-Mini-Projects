'''
Author:Keerthi Nivasshini Thangaraj
FileName:CypherText_keerthi_04.py
Pupose:Compute encryption scheme - alphabetic character into number
Revision:
    00: Announce and read the input values in the form of string.
    01: The string entered by the user must be converted to lowercase before generating the code for each letter.
    02: Use for loop to traverse the string so each character can be isolated in sequence.
    03: Use the ord() built-in function to convert each character to the number.
    04: Print the output value.
'''
print("Program to encode a word")

#Announce and read the input values in the form of string
string=str(input("Enter a word: "))

#Initialize variables
i=0
code=0

#Convert the input string to lowercase letters
string=string.lower()

#Perform operations within for loop to convert character into code
for i in string:
    code=ord(i)-97
    #print output code for the user view
    print(code,end=' ')

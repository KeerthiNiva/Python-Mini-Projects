'''
Program: Fstring Exercises
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to complete 10 Exercises on Fstring
Revision: First Revision of the fstring exercise

'''
#Program Announcement
print("\n Exercises on Fstring \n")
# f-string exercises (NO HARDCODING!)
# EDIT ONLY THE ASSIGNMENT STATEMENTS INDICATED
# LEAVE EVERYTHING ELSE AS IT IS
# x, y, z variables for the exercise
x = 27
y = 3.14159
z = 'pi'
# build f-strings to each specification below
# 10 different exercises of increasing complexity

''' #1
Create a string variable s that uses
variable x to create this string ...
"27 is a whole number"
'''
# edit the assignment statement below
s = f'{x} is a whole number'
print(f"#1 ...\n{s}")

''' #2
Create a string variable s that uses variable x
and the type() function to create this string ...
"27 is <class 'int'>"
'''
# edit the assignment statement below
s = f'{x} is {int}'
print(f"#2 ...\n{s}")

''' #3
Create a string variable q that uses
variable y to create this string ...
"pi to 6 digits is 3.14159"
'''
# edit the assignment statement below
q = f'pi to 6 digits is {y}'
print(f"#3 ...\n{q}")

''' #4
Create a string variable q that uses
variable y to create this string ...
"pi to 3 digits is 3.14"
'''
# edit the assignment statement below
q = f'pi to 3 digits is {y:.2f}'
print(f"#4 ...\n{q}")

''' #5
Create a string variable r that uses
variables y and z to create this string ...
"pi to 4 digits is 3.142"
'''
# edit the assignment statement below
r = f'{z} to 4 digits is {y:.3f}'
print(f"#5 ...\n{r}")

''' #6
Create a string variable r that uses variables x,
y, and z to create this output ...
"    27     3.14159      pi    "
Each variable is centered across 10 spaces
'''
# edit the assignment statement below
r = f'{x:^10}{y:^10}{z:^10}'
print(f"#6 ...\n{r}")

''' #7
Create a string variable r that uses variables x,
y, and z to create this table ...
"    x         y         z     
     27     3.14159      pi   "
Each item is centered across 10 spaces.
Use the newline escape sequence as needed.
'''
# edit the assignment statement below
r = f"{'x':^10}{'y':^10}{'z':^10}\n{x:^10}{y:^10}{z:^10}"
print(f"#7 ...\n{r}")

''' #8
Create a string variable q that uses variables x and
y as US currency (two decimal places, preceded
by a dollar sign, left justified across 10 spaces ...
"$27.00    $3.14     "
'''
# edit the assignment statement below
q = f'${x:<10.2f}${y:<10.2f}'
print(f"#8 ...\n{q}")

''' #9
Create a string variable q that uses variables x and
y as US currency (two decimal places, preceded
by a dollar sign, center justified across 10 spaces ...
"  $27.00    $3.14   "
'''
# edit the assignment statement below
q = f"{f'${x:.2f}':^10}{f'${y:.2f}':^10}"
print(f"#9 ...\n{q}")

''' #10
Create a string variable s that uses variables x and
y as US currency (two decimal places, with room for
4 digits left of the decimal point preceded
by a dollar sign and center justified across 10 spaces ...
" $  27.00  $   3.14 "
'''
# edit the assignment statement below
s =f"{f'${x:7.2f}':^10}{f'${y:7.2f}':^10}"
print(f"#10 ...\n{s}") 






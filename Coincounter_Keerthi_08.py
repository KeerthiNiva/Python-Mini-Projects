"""
Program: Coin Counter
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to count coins and calculate the values
Revision: First Revision of the Coin Counter Program

"""
#Program Annoucement
print("\n***Program to count coins and calculate the values***\n")
#Getting the coin string from the user
s = input("Enter the String: ")
#Assigning variables for all coin types to calculations of the values
p_amt= s.count("p")*0.01
n_amt= s.count("n")*0.05
d_amt=s.count("d")*0.10
q_amt= s.count("q")*0.25
h_amt= s.count("h")*0.50
#Calculating total amount from adding values of all the coin types
Total_amt=p_amt+d_amt+n_amt+q_amt+h_amt
#Printing the output using f string to yield a coin report table
print(f'\n{"="*36:^36}\n {"Coin Counter Report":^36} \n{"="*36:^36}')
print(f'\n{" "}\n{"Coin":<12}{"Value":^9}{"Number":^8}{"Amount":^8}')
print(f'{"="*4:<12}{"="*5:^9}{"="*6:^8}{"="*6:^8}')
print(f'{"Pennies":<12}{"$0.01":^9}{s.count("p"):^8}{f"${p_amt:5.2f}":^8}')
print(f'{"Nickles":<12}{"$0.05":^9}{s.count("n"):^8}{f"${n_amt:5.2f}":^8}')
print(f'{"Dimes":<12}{"$0.10":^9}{s.count("d"):^8}{f"${d_amt:5.2f}":^8}')
print(f'{"Quarters":<12}{"$0.25":^9}{s.count("q"):^8}{f"${q_amt:5.2f}":^8}')
print(f'{"Half-Dollars":<12}{"$0.50":^9}{s.count("h"):^8}{f"${h_amt:5.2f}":^8}')
print(f'{"Total Amount: ":>30}{f"${Total_amt:5.2f}"}')


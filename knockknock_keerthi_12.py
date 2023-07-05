"""
Program: Knock-Knock
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to tell knock-Knock Jokes
Revision: First Revision of the Knock-Knock

"""
#Importing random module to shuffle the jokes
import random as rn

#Program Announcement
print("\n*** Program to tell knock-Knock Jokes***\n")
#Defining function to prompt, response of knock-knock and WHo's there
def promptresponse(prompt,responses,suggest):
    #Running through while to check for the response variants from the user
    while True:
        print(prompt)
        response= input()
        #Checking for response variant with case sensitive and punctuation agnostic
        if response.strip("?!""'',-.").lower() in responses:
            break
        else:
            #Suggesting right response if the response variant is not matched
            print(f"The Correct response is {suggest}\nTry Again")
           
#Assigning response variants list to check from users input
resp_list1 = ['whos there','who there','whos dere',"who's there?","who is there"]
#Assigning list for jokes
jokelist = [('Leon',"Leon me when you’re not strong!"),('Quiche',"Can I have a hug and a quiche?"),('A leaf',"A leaf you alone if you leaf me alone.")
            ,('Tiss',"A Tiss-who is for blowing your nose"),('Double',"W!"),('Candice',"Candice joke get any worse?!"),('Olive',"Olive next door. Hi neighbor!")]
print(f"Ready to tell a Knock-Knock joke!\n\nThere are {len(jokelist)} Available.")
#Assiginin  totaljokes variable to users response on how many jokes to tell
totaljokes=int(input("How many jokes you want me to tell: "))
#Validating users response for number of jokes
if totaljokes>len(jokelist) or totaljokes<=0:
    print(f"The number must be in the range: 1 to {len(jokelist)}")
    totaljokes=int(input("\nHow many jokes you want me to tell? "))
else:
    pass
#printing how many jokes to be told
print(f"\nReady to tell {totaljokes} jokes!\n{'-'*40}")
#using shuffle method to tell jokes randomly
rn.shuffle(jokelist)
#Traversing through for loop on the jokes list with required number of jokes
for x in  (jokelist[:totaljokes]):
    #using the function prompt response for responses 
    promptresponse('\nKnock-Knock',resp_list1,"'who's there?'\n")
    promptresponse(f'{x[0]}',[f'{x[0]} who?'.strip("?!""'',-.").lower()],f"'{x[0]} who?'\n")
    print(f"{x[1]}\n{'-'*40}")
print("\nThank you Play Again")

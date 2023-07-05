"""
Program: Language Translation by Dictionary
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to translate words from English to French and vice-versa using 
Revision: First Revision of Language Translation by Dictionary

"""
#Program Announcement
print("\n***Program to translate words from English to French and vice-versa***")
#Creating List of words for English and French
english = ['chicken','salt','apple','earth','bean','water','milk']
french = ['poulet','sel','pomme','terre','haricot','eau','lait']
#Using the list we are creating the dictionary
translator = dict(zip(english,french))
#Creating while loop to run through user input and recieve response until the it is true
while True:
    #Getting The Response from user for a word to Translate
    resp = input("\nEnter the english or french word to translate: ")
    if resp =='':
        print("Exiting....")
        break
    else:
        for eng,french in translator.items():
        #Checking for the word in english list and printing the french word for it
            if resp==eng:
                print(f"The french word '{french}' is '{resp}' in english")
                break
            #Else Checking for the word in french list and printing the french word for it
            elif resp==french:
                print(f"The english word {eng} is {resp} in french")
                break
        #If the word is not in the dictionary then printing the set of statements to add it to the list based on the language
        else:
            print(f"\nThe word {resp} was not found in the english or french word list")
            resp_2=input("would you like to add to the dictionary? <y>es or <n>o ")
            #Statements to check whether if user wants to add the word to the dictionary or not
            if resp_2.lower()=='n' or resp_2.lower()=='':
                print(f"The word {resp} is not added to dictionary")
            elif resp_2.lower()=='y':
                #while loop is created to handle if user enters invalid input at this stage of the program
                while True:
                    resp_3=input(f"what language is {resp} in <E>nglish or <F>rench ")
                    if resp_3.lower()=='f':
                        eng_add=input(f"What is the english word for '{resp}'? ")
                        translator[resp]=eng_add
                        break
                    elif resp_3.lower()=='e':
                        french_add=input(f"What is the french word for '{resp}'? ")
                        translator[resp]=french_add
                        break
                    else:
                        print("Invalid Input! Try Again\n")
            

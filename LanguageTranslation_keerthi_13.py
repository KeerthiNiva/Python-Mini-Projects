"""
Program: Language Translation
Author: Keerthi Nivasshini
Progam Description: Program to translate words from English to French and vice-versa
Revision: First Revision of Language Translation

"""
#Program Announcement
print("\n***Program to translate words from English to French and vice-versa***")
#Creating List of words for English and French
english = ['chicken','salt','apple','earth','bean','water','milk']
french = ['pulet','sel','pomme','terre','haricot','eau','lait']
#Creating while loop to run through user input and recieve response until the it is true
while True:
    #Getting The Response from user for a word to Translate
    resp = input("\nEnter the english or french word to translate: ")
    #Checking for the word in english list and printing the french word for it
    if resp.lower() in english:
        eng_ind= english.index(resp)
        print(f"The french word '{french[eng_ind]}' is '{english[eng_ind]}' in english")
    #Else Checking for the word in french list and printing the french word for it
    elif resp.lower() in french:
        french_ind= french.index(resp)
        print(f"The english word {english[french_ind]} is {french[french_ind]} in french")
    #Cheching for null string from user and breaking the loop and exiting the program
    elif resp =='':
        print("Exiting....")
        break
    #If the word is not in the dictionary then printing the set of statements and to add it to the list based on the language
    else:
        print(f"\nThe word {resp} was not found in the english or french word list")
        resp_2=input("would you like to add to the list? <y>es or <n>o ")
        if resp_2.lower()=='n':
            pass
        elif resp_2.lower()=='y':
            resp_3=input(f"what language is {resp} in <E>nglish or <F>rench ")
            if resp_3.lower()=='f':
                eng_add=input(f"What is the english word for '{resp}'? ")
                french.append(resp)
                english.append(eng_add)
            elif resp_3.lower()=='e':
                french_add=input(f"What is the french word for '{resp}'? ")
                english.append(resp)
                french.append(french_add)
                
        
    
                 
    



             
    

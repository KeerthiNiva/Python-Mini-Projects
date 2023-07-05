"""
Program: Ultimate Language Translation
Author:  Keerthi Nivasshini
Progam Description: Program to translate words from English to French and vice-versa using 
Revision: First Revision of Ultimate Language Translation

"""

#Function definition to translate word, add to dictionary & saving it to the file  
def wordAdd(Lang,wrd,datadict,fname):
    '''Function to add translate & add to dictionary, save it to the file 
       Lang : Language to translate, wrd : wrd to be translated, 
       datadict: dictionary to add the translated word fname: file name with extension to save the dictionary'''
    a=input(f"What is the {Lang} word for '{resp}'? ")
    if a=='':
        print("Exiting....")
        return False
    else:
        datadict[resp]=a
        with open(fname,'w') as f:
            for key in datadict:
                f.write(f'{key} {datadict[key]}\n')
        f.close()
        print(f"\nThe word '{wrd}' added to the dictionary with translation.\n{'='*60}\n")
        return True
            
#Program Announcement
print("\n***Program to translate words from English to French and vice-versa***")
#Opening the file and reading the data
with open('vocabulary.txt') as f: 
    data= f.readlines()
#Listcomphrension to get list of tuples from the data
datatuples = [tuple(i.split()) for i in data if len(i.strip())!=0 ]
#Casting the tuples to dictionary
translator = dict(datatuples)
#Assigng true to the outerloop variable to control the while loop
outerloop=True
while outerloop:
    #Getting The Response from user for a word to Translate
    resp = input("\nEnter the english or french word to translate: ")
    if resp =='':
        print("Exiting....")
        break
    else:
        #Iterating the Dicitonary t
        for eng,french in translator.items():
        #Checking for the word in dictionary and printing the equalent translation in french or english
            if resp==eng:
                print(f"The french word '{french}' is '{resp}' in english")
                break
            elif resp==french:
                print(f"The english word '{eng}' is '{resp}' in french")
                break
        #If the word is not in the dictionary then printing the set of statements to add it to the list based on the language
        else:
            print(f"\nThe word '{resp}' was not found in the english or french word list")
            while True:
                    resp_2=input("would you like to add to the dictionary? <y>es or <n>o ")
                    #Statements to check whether if user wants to add the word to the dictionary and perform operations
                    if resp_2=='':
                        print("Exiting....")
                        outerloop=False
                        break
                    elif resp_2.lower()=='n':
                        break
                    elif resp_2.lower()=='y':
                        while True:
                                    #Getting language of the word as an input from the user
                                    resp_3=input(f"what language is '{resp}' in <E>nglish or <F>rench ")
                                    if resp_3=='':
                                        print("Exiting...")
                                        outerloop=False
                                        break
                                    #Operations to add french word by calling the function
                                    elif resp_3.lower()=='f':
                                        outerloop=wordAdd('English',resp,translator,'vocabulary.txt')
                                        break
                                    #Operations to add english word by calling the function
                                    elif resp_3.lower()=='e':
                                        outerloop=wordAdd('French',resp,translator,'vocabulary.txt')
                                        break
                                    else :
                                        print('\nInvalid Input! It should be "E" or "F",  Try Again .')
                        break
                    else:
                        print('\nInvalid Input! It should be "Y" or "N",  Try Again .')
                
                

"""
Program: Language Translation by Dictionary
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to translate colours with multiple languages using dictionaries
Revision: First Revision of Language Translation by Dictionary

"""

colors = {}
colors['red'] = {}
colors['red'].update({'french':'rouge'})
colors['red'].update({'spanish':'rojo'})
colors['red'].update({'german':'rot'})
colors['green'] = {}
colors['green'].update({'french':'vert'})
colors['green'].update({'spanish':'verde'})
colors['green'].update({'german':'grun'})
colors['yellow'] = {}
colors['yellow'].update({'french':'jaune'})
colors['yellow'].update({'spanish':'amarillo'})
colors['yellow'].update({'german':'gelb'})
colors['blue'] = {}
colors['blue'].update({'french':'bleu'})
colors['blue'].update({'spanish':'azul'})
colors['blue'].update({'german':'blau'})

#Program announcement
print("Language Translator")   

#Initiating 'while True' loop to continuously get colours from users
while True:   
    print(f"\nAvailable colours are: {'; '.join([k for k in colors.keys()])}")
    colour = input("Please enter a colour name: ").lower()
    if colour in colors.keys():
        #create conditions to look up and return the respective colour
        print('Available language translations are: german; french; spanish')
        if (language := input('Please enter a language from the list: ').lower()) in colors['red'].keys():
            print(f"The colour '{colour}' in {language.capitalize()} is '{colors[colour][language]}'.")
        else:
            print(f"Language '{language.capitalize()}' was not found. Please try again!")
    elif colour == '':
        print('Exiting ...')
        #Break to exit the loop
        break
    else:
        #Adding new colours
        if input(f"The English colour '{colour}' was not found. Would you like to add '{colour}' to the dictionary? <y>es or <n>o ").lower() in ['y','yes']:
            colors[f"{colour}"] = {}
            colors[f"{colour}"].update({'french': (input(f"What is the French colour for {colour}? ")).lower()})
            colors[f"{colour}"].update({'spanish': (input(f"What is the Spanish colour for {colour}? ")).lower()})
            colors[f"{colour}"].update({'german': (input(f"What is the German colour for {colour}? ")).lower()})
            print('The new colours have been added to the dictionary!')
        else:
            print('Let\'s try again!')


'''
Author:Keerthi Nivasshini Thangaraj
FileName:letterGrades_keerthi_02.py
Pupose: To calculate the grade for score
Revision:02
'''
#defining function for calculating letterGrade
def letterGrade(score):
    if score>=95:
        return "A+"
    elif score>=90 and score<95:
        return "A"
    elif score>=85 and score<90:
        return "A-"
    elif score>=80 and score<85:
        return "B+"
    elif score>=75 and score<80:
        return "B"
    elif score>=70 and score<75:
        return "B-"
    elif score>=65 and score<70:
        return "C+"
    elif score>=60 and score<65:
        return "C"
    elif score>=55 and score<60:
        return "C-"
    elif score<55:
        return "F"
    
#getting input score from the user
score=float(input("Enter the Numerical Score:"))

#print the letterGrade value returned from the above function
print("The letter grade for",score,"percent is", letterGrade(score), ".")

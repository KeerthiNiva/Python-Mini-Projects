"""
Program: Phloog'sClass_keerthi_11
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program To Calculate Grades using function
Revision: First Revision of Dr.Phloog's Class

"""
#Program Announcement
print("\n*** Program to calculate grades for Dr. Phloog ***\n")
#Definng function to return average and grade letters for the grades
def findGrade(grades):
    #Sortting number in descending order
    grades.sort(reverse=True)
    #Excluding the lowest grades from 1 out of 3
    grades= grades[:-(len(grades)//3)]
    #Assing the average variable and computing it
    average=float(sum(grades)/len(grades))
    #Assigning the string variable Letter
    letter =''
    #Assigning appropriate letter based on the grade as per Dr.phloog's criteria
    if average<80:
        letter = 'X'
    elif average>90:
        letter = 'Z'
    else:
        letter = 'Y'
    #Returning the average and letter to the grade
    return(average,letter)

#Assinging an Empty list
gradeList = []
#Testing the function with grades appended to the gradeList
gradeList.append([50,100,60]) # [80.00,'Y']
gradeList.append([50,100,50,50,100,50,50,100,50]) # [75.00,'X']
gradeList.append([65,100,22,89,0,100,92,78,87,97]) # [91.86,'Z']
gradeList.append([90,70,60,100,65,95,27,55,79,60]) # [79.86,'X']
gradeList.append([65,100,22,89,45,92,78,87]) # [85.17,'Y']
#Iterating each item in the gradeList to test the function
for item in gradeList:
    grade = findGrade(item)
    #Printing the output
    print(f"{grade[0]:6.2f} --> {grade[1]} ")  


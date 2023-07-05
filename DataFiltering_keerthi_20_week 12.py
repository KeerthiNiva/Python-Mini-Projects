"""
Program: Produce Exercise
Author: Keerthi Nivasshini Thangaraj
Progam Description: Data Handling Exercise
Revision: First Revision of Data Filtering Challenges
"""


#Importing CSV Module to work with csv files
import csv

#Program Announcement
print("\n***Program to solve Data Filtering Challenges***\n")

#Formatting data into easily accessbile format to analyze and filter
data = []
csvfile = open('produce_extra.csv','r')
reader = csv.reader(csvfile)
for row in reader:  ###! main loop reads one row at a time
    if reader.line_num == 1: ###! get the location names from row 1
        locations = row[2:]  ###! slice to remove commodity and date
    else:
        for location,value in zip(locations,row[2:]):  ###! iterate through locations and values
            row_num = len(data)     ###! index for the data row 
            data.append(row[:2])    ###! new data row: commodity and date
            data[row_num].append(location)  ###! append location
            data[row_num].append(float(value.replace('$','')))     ###! append value
csvfile.close()



# (1) make a list named comList of all commodities using list comprehension
#  (one source code statement)

comList = [i[0] for i in data]

# (2) make another list named uComList with the duplicates removed 
# (one source code statement) hint: use the set() and list() functions 

uComList = list(set([i[0] for i in data]))


# (3) Print the number of unique commodities that are present in the data
# (one source code statement) hint: use the len() function
print(f'There are {len(uComList)} unique commodities.')

# (4) Use list comprehension compute a list named comNums where each item is a list 
# of this format: [commodity_name, number of records of that commodity]
# (one source code statement) hint: use the count() method


comNums = [[i,comList.count(i)] for i in uComList]

# (5) for each item in comNums, print the number of records
# (two source code lines) 
####
for i in comNums:
    print(f'Found {i[1]} records for {i[0]}')


# (6) Sort comNums according to number of records in ascending order 
# (one source code statement) hint: use the sort() method with a lambda

comNums.sort(key= lambda a:a[1])

# (7) print the commodity with the fewest number of records
# (one source code statement)

print(f'Least available commodity = {comNums[0][0]}.')

# (8) print the number of weeks the least available commodity was available for
# (one source code statement) hint: each commodity has 5 records for each week
print(f'{comNums[0][0]} were available for {comNums[0][1]//5} weeks.')

# (9) use a list comprehension to find the lowest price for nectarines in Chicago
# assign it to a variable called min1 hint: use the min() function
# (one source code statement)

min1= min([i[3] for i in data if i[0]=='Nectarines' and i[2]=="Chicago"])


# (10) use a list comprehension to find the date of the lowest price for nectarines 
# in Chicago and assign it to a variable named mind1 
# (one source code statement) hint: one value at index=0

mind1 = min([[j[3],j[1]] for j in data if j[0]=="Nectarines" and j[2]=="Chicago"],key = lambda a:a[0])[1]


# (11) print the lowest price for nectarines in Chicago and the date
# (one source code statement)
print(f'The lowest price for Nectarines in Chicago was {min1} on {mind1}')


# (12) use a list comprehension to find the farm price for nectarines on the same 
# date and assign it to a variable named fp1
# (one source code statement) 


fp1 = [i[3] for i in data if i[0]=="Nectarines" and i[2] == "Farm" and i[1]==mind1][0]


# (13) print the farm price for nectarines on the date 
# of lowest price in Chicago and print the computed price difference
# (one source code statement)

print(f'Nectarine farm price on {mind1} was {fp1}; ${min1-fp1:.2f} less than in Chicago.')


# (14) Create a dictionary called comNumsDict where the keys are the commodities 
# and the values are the number of weeks each commodity was available for
# (one source code statement) hint: use a list comprehension and the dict() function
comNumDict= dict([(i[0],i[1]//5) for i in comNums])


# (15) Use comNumDict to print the number of weeks peaches were available for
# (one source code statement)

print(f'Peaches where available for {comNumDict["Peaches"]} weeks.')

# (16) Use a list comprehension to calculate the average price of Peaches
# in Atlanta and assign it to a variable pAvg
# (one source code statement) hint use the sum() function and the dictionary

pAvg= sum([i[3] for i in data if i[0]=="Peaches" and i[2]=="Atlanta"])/comNumDict["Peaches"]

# (17) Print the average price of Peaches in Atlanta
####

print(f'The average price of peaches in Atlanta was ${pAvg:.2f}.')

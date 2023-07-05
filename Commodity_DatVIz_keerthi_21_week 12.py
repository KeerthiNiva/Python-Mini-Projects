"""
Program: Commodity Data, Filtering & Visualization
Author: Keerthi Nivasshini Thangaraj
Progam Description: Program to Filter and visualize the commodity data 
Revision: First Revision of DataFiltering_Visualization

"""
#Importing the required libraries and modules
import csv as f
from datetime import datetime as d

#Program Announcement
print("\n***Program to Filter and visualize the commodity data***")

#Reading the file and storing the data
with open('produce_csv.csv','r') as csvfile:
    reader= f.reader(csvfile)
    data = [row for row in reader]

#Modifying the data into required format to filter and analyze  
moddata = []
for i in data:
        innerlist =list()
        for val in i:
            if "$" in val:
                    #Replacing the $ string in the price with null string and converting the price from text to float
                innerlist.append(float(val.strip().replace("$","")))     
            elif "/" in val:
                    #Converting the date string to datetime format 
                innerlist.append(d.strptime(val,'%m/%d/%Y'))
            else:
                innerlist.append(val)
        moddata.append(innerlist)

#Only Locations are popped out from modified data
locations = moddata.pop(0)[2:]

#New list records is created in order to be in format of (Commodity,Date,Location, Price ) so that it is used for analysis
records =  list()
for row in moddata:
    newrow = row[:2]
    for loc,price in zip(locations,row[2:]):
        records.append(newrow+[loc,price])
        
#Data Selection is done to analyze
select = list(filter(lambda x: x[0]=="Oranges" and x[2]=="Chicago",records))

dates= [i[1] for i in select]
price = [i[3] for i in select]

#Dates and Price are together placed to make good visuals of price over the time period
vizlist= [[d,p] for d,p in zip(dates,price)]
#Date is sorted to make sure it chronological
vizlist.sort(key= lambda a: a[0])

#Vector Graph is printed for dates and prices
for i in vizlist:
    print(f'{d.strftime(i[0],"%m-%d-%Y")} {int(i[1]*25)*"="}')

#importing modules for visualization
import matplotlib.pyplot as plt
import matplotlib.ticker as tk


#Using matplotlib modules to visualize the data
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(dates,price,label="Oranges in Chicago",color='b')

#Axis labels are set for x and y axis
ax.set_xlabel('Date')
ax.set_ylabel('Price in Dollars')
#Formating is done for price such that it is in 2 decimal and with dollars
fmt='${x:,.2f}'
tick = tk.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
plt.legend()
plt.show()

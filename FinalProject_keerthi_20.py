"""
Program: Final Project
Author: Keerthi Nivasshini
Progam Description: Program to Analyze the Commodity Data
Revision: First Revision of Final Project

"""
#Importing the Required Modules
import csv as f
from datetime import datetime as d
import plotly.offline as py
import plotly.graph_objs as go
import statistics as s

#Defining the required Functions
def columnPrint(x,enum=0,wid=20,col=3):
    '''
    one location(Loop) with selected products
    x : List of strings to print
    enum : Space allocated for the index to print. The default is 0.
    wid : Width space of the one element. The default is 20.
    col : Total Number of columns to print. The default is 3.
    '''
    s=''
    for n,item in enumerate(x):
        if len(s)<col*(wid+enum+2):
            if enum:
                s+=f'<{n:{enum}}>'
            s += f' {item:<20}'
        else:
            print(s)
            s=''
            if enum:
                s += f'<{n:{enum}}>'
            s += f' {item:<20}'
    if s:
            print(s)
        
def selectList(x,LisName):
    '''
    #Defining Function to prompt the user to input index number and returning a list of selected elements
    X = List which is prompted to choose
    LisName = Name of list ('Date','Product','Locations')
    '''
    
    x.sort()
    print('\n')
    if LisName.strip().lower()=='date': #Performing operations separately for the date as LisName
        columnPrint(x,2,col=5)
        print(f'Earliest available date is: {min(x)} \nLatest available date is: {max(x)}')
        a = input('Enter the start/end  date number separated by spaces: ').split()
        printlis = [v for i,v in enumerate(x) if str(i) in a]
        lis = [d.strptime(v, '%Y-%m-%d') for i,v in enumerate(x) if i>=int(a[0]) and  i<=int(a[1])]
        print(f"Selected : {' to '.join(printlis)}")
    else: #Performing operations separately for the list other than date as LisName
        columnPrint(x,2)
        a = input(f'Enter the {LisName} number separated by spaces: ').split()
        lis = [v for i,v in enumerate(x) if str(i) in a]
        print(f"Selected {LisName}: {' '.join(lis)}")
    lis.sort()
    return lis

#Program Announcement
print(f'{"="*30}\n{"Analysis of Commodity Data":^30}\n{"="*30}\n') 

with open('produce_csv.csv','r') as csvfile: #Reading the file and storing the data
    reader= f.reader(csvfile)
    data = [row for row in reader]


moddata = []  #Modfying data into useable format and storing it in moddata
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
 
locations_lis= moddata.pop(0)[2:] #Poping  locations separately 

#Creating records with location on it so that each product has number of records based on the no of locations
records=[]
for row in moddata:
    newrow = row[:2]
    for loc,price in zip(locations_lis,row[2:]):
        records.append(newrow+[loc,price])
        
        
products_lis = list(set([i[0] for i in records])) #Getting the products seperately to print to the user for input
date_lis = list(set([d.strftime(i[1],'%Y-%m-%d') for i in records])) #Getting the dates seperately to print to the user for input

#Getting the list based on user's choice
print('\nSELECT PRODUCT BY NUMBER ...')
selected_products=selectList(products_lis,'Product') #Calling the selectList function to get the list of products
print('\nSELECT DATE RANGE BY NUMBER ...')
selected_dates=selectList(date_lis,'date') #Calling the selectList function to get the list of dates
print('\nSELECT LOCATIONS BY NUMBER ...')
selected_locations = selectList(locations_lis,'location') #Calling the selectList function to get the list of location

#Filtering the original records based on the user requirement
datafiltered = list (filter(lambda v:v[0] in selected_products and v[1] in selected_dates 
                            and v[2] in selected_locations,records))


#Creating a Dictionary called avg_dict for getting the avg prices for each combo of (Product, Location)
avg_dict={}                                                
for prod in selected_products:
    avg_dict[prod]={}  #Creating another dictionary for each product
    for loc in  selected_locations:
        avg_dict[prod].update({loc:[]}) # Creating an empty list as value for each location within the prod dict
        avg_dict[prod][loc]=s.mean([x[3] for x in datafiltered if x[2]== loc and x[0]== prod])

#Creating the empty list trace for appending traces (For each each product chosen)
trace=[]        
for i in selected_locations:
    y_Price = [] #the list y_price is created
    for prod in avg_dict:
        # Appending price from avg_dict to y_price for one location(Loop) with selected products
        y_Price.append(avg_dict[prod][i])
    traces = go.Bar(x = [i for i in avg_dict], y = y_Price,name = i) #Bar object is created for one location(Loop) with selected products 
    trace.append(traces)# Appending the Created bar object with the trace list


#Formatting the layout for Bar Graph
layout = go.Layout(barmode = 'group', 
                   title = f'Produce Prices from {d.strftime(selected_dates[0],"%Y-%m-%d")} through {d.strftime(selected_dates[1],"%Y-%m-%d")}',
                   yaxis = dict(title = 'Average Price', tickformat = '$.2f'), xaxis = dict(title = 'Product'))

#Ploting the Figure
fig = go.Figure(data= trace,layout=layout)
py.plot(fig,filename= 'Grouped-Bar-keerthi.html')

   
    
    
    
    
    


        


        


        
    


















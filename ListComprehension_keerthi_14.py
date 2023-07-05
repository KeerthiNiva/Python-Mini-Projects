"""
Program: listCompSort
Author: Keerthi Nivasshini
Progam Description: exercises on list comphreshion and sort
Revision: First Revision of the listCompSort

"""

#Program Announcement
print("\n***Exercises on list comphreshions***\n")
###### 1. List comprehension analysis
### Code
def linc(a,b=2):
    '''The Function linc takes list <a> as an arguement and add the second arguement <b> as increment value
       to each element in the list if and only the element is of type int and creates a new list,
       by default the increment arguement <b> is 2'''
    return[i+b for i in a if type(i) is int]
x = [1,2,'3',4]
y = linc(x)  # [3,4,6]
z = linc(x,1) # [2,3,5]
print(x)
print(y)
print(z)

###### 2. the listInc() function
def listInc(a):
    '''The Function listInc takes list <a> as an arguement and increment by 1
       to each element in the list if and only the element is of type int and returns a new list'''
    return[i+1 for i in a if type(i) is int]  
### listInc() tests
assert listInc([7,2,4,8]) == [8,3,5,9], 'listInc failed [7,2,4,8]'
assert listInc([9,-1,0.0,5]) == [10,0,6], 'listInc failed [9,-1,0.0,5]'
print('listInc is OK\n')

###### 3. the listOut() function
def listOut(a):
    ''' listOut takes a list <a> as an arguement and prints each element in the list'''
    return[print(i) for i in a]
### listOut() tests
listOut([7,2,'OK',8])
print()
listOut([[1,2],2.0,'$',8])
print()

###### 4. statements that move items between lists
### end of A to beginning of B
a,b = [1,2,3], [4,5,6]
b.insert(0,a.pop(-1))
print(a,b)
### beginning of A to end of B
a,b = [1,2,3], [4,5,6]
b.append(a.pop(0))
print(a,b,'\n')


###### 5a. the rotateForward() function
def rotateForward(a):
    '''rotateForward function takes a list as arguement and returns the list by changing the postions of the last element to the first postion
        and all the other elements are forwarded by 1 step'''
    return [a[(i-1)%len(a)] for i,x in enumerate(a)]
#rotateForward([1,2,3,4])
### rotateForward() tests
assert rotateForward([1,2,3,4,5]) == [5,1,2,3,4], 'rotateForward failed'
assert rotateForward([17,'ok',0.0,'x'])== ['x',17,'ok',0.0], 'rotateForward failed'
print('rotateForward ok\n')

###### 5b. the rotateBackward() function
def rotateBackward(a):
        '''
        rotateBackward function takes a list as arguement and returns the list by changing the postions of the first element to the last postion
        and all the other elements are backwarded by 1 step
        '''
        return [a[(i+1)%len(a)] for i,x in enumerate(a)]
### rotateBackward() tests
assert rotateBackward([1,2,3,4]) == [2,3,4,1], 'rotateBackward failed'
assert rotateBackward([17,'ok',0.0,'x']) == ['ok',0.0,'x',17], 'rotateBackward failed'
print('rotateBackward ok\n')

###### 6. Analysis of iSort()
def iSort(x,n=2):
    '''
    The function iSort() takes an list of tuples as an arguement and sort the list by specified index of tuple as second argument
    by default the second argument n is 2=
    '''
    return sorted(x,key= lambda a: a[n])
x = [(1,'one','uno'),(2,'two','dos'),(3,'three','tres')]
#Tescases for iSort
print(iSort(x))
print(iSort(x,1))
print()


###### 7. Length sorting
z = ['bzz','z','cz','azzz']
z.sort(key=len)
print(z,'\n')


###### 8. the backSort() function
def backSort(a):
    '''backSort function takes list of strings as an arguement and returns the same list sorted by last letter of each string element in the list'''
    return sorted(a,key= lambda a: a[-1])
### backSort() tests
assert backSort(['red','yellow','blue','green','black']) ==['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
assert backSort(['cbb','reda','purpled','blackc','white']) ==['reda', 'cbb', 'blackc', 'purpled', 'white'], 'backSort FAILED'
print('backSort OK')









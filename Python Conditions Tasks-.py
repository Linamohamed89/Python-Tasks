#Python Conditions Tasks

#1. Check if 10 is bigger than 15 or not


x=10
if x>15:
    print('x is not bigger than 15')

#2. If 10 is not bigger than15 print x is smaller than 15

x=10
if x<15:
    print('x is smaller than 15')
    
#3. In which cases we will use all

x,y,z=2,4,6
if all([x==2,y==4,z==6]):
    print(True)


#4. What is the differences between all , and

x=5
y=6
z=7

#and
if x==5 and y==6 and z==7:
    print('welcome')

#all
if all([x==5 , y==6 , z==7]):
    print('Hello')


#all +([ , , ])


#5. What is the differences between any , or

userrname='Lina'
password=1234
#or
if userrname=='Lina' or password==1234:
    print('Hi Lina')

#any
    if any ([userrname=='Lina' , password==1234]):
        print('not found')

#any +([ , , ])
        



#6. If we need all the conditions to be true we will use ....
'''
L='Lina'
B='Bisherr'
M='Margana'

if all ([L=='Lina',B=='Bisherr',M=='Margana']):
    print(True)
'''


#7. What is the differences between if , elif

print("the code always checks to see if an 'if' statement is true, checks 'elif' statements only if each 'if' and 'elif' statement above it is false")

#8. What is the differences between elif else

print("The elif allows us to tie multiple if statements together but else runs only when the conditions for all attached if and elif statements are false.")


#9. Can we use more than one elif

print('yes , we can ')

#10. Can we use more than one else

print('no , we can not')

#11. write s simple ternary operator

movieRate=18
age=18
print('Movie is Not Good 4U' if age < movieRate else 'Movie is Good 4U And Happy Watching')

'''
if age < movieRate:
    print('Movie is Not Good 4U')
els:
    print('Movie is Good 4U And Happy Watching')
'''
#12. in elif , python will check all the conditions no matter what ?


print('just in the case of if ')


#13. in elif we use else for ... ?


#14. if we have this list [2,4,6,8,10] :
    #1. check to see if 4 in this list or not

list=[2,4,6,8,10]
if 4 in list:
    print('4 in this list')

#2. check to see if 4 and 6 in this list on not

list=[2,4,6,8,10]
if 4 and 6 in list:
    print('4,6 in this list')

#3. check to see if 3 or 6 in this list

list=[2,4,6,8,10]
if 3 or 6 in list:
    print('Hello')

#4. check to see if 2 , 4 and 5 in this list Python Conditions Tasks

list=[2,4,6,8,10]
if all([2,4,5]) in list:
    print('Python Conditions tasks')

else:
    print('not found')

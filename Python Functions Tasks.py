


#Python Functions Tasks


#1. Create a simple function that takes 2 numbers and print their values

def mynummber (x,y):
    print(x+y)

mynummber(3,4)

#2. Create a simple function that takes 2 numbers and return their values

def mynummber (x,y):
    return x-y
   

L=mynummber(3,4)
print(L)

#3. In the above return function , use keyword arguments when calling the function

def mysum2(x,y):
    return x , y

a=mysum2(y=7,x=3)
print(a)

#4. In the above return function , give x and y default values of 0 and call the function with no arguments

def mysum2(x=0,y=0):
    return x ,y
a=mysum2()
print(a)

#5. Create a function that can take any number of arguments and print the sum of them


def mysum2(x=0,y=0):
    return x ,y
a=mysum2(3,7)
print(a)




#6. Create the same sum function using the lambda

hello= lambda name :f"Hello {name}"
print(hello("ahmed"))


#7. Call the lambda function at the same definition line

hello= lambda name :f"Hello {name}";print(hello("ahmed"))

#8. Write the difference between the local variable and global variable


start,end=1,100
for num in range(start,end+1):
    if num %2==0 :
        print(num,end=" ")


print('----------------------------')


# Python program to print Even Numbers in given range
# using while loop

max = 100
num = 1

while num <= max:
    if(num % 2 == 0):
        print("{0}".format(num))
    num = num + 1


print('----------------------------')


class Task:
    def with_f(self):
        even=[]
        odd=[]
        for x in range(1,101):
            if x %2==0:
                even.append(x)
            else:
                odd.append(x)

        print(even)
        print(odd)

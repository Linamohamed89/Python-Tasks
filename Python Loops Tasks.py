

#Python Loops Tasks


#1. Print numbers from 0 to 10 using while

h=0
while h <= 10:
    print(h)
    h +=1

print('-------------------------------------')
    
#2. Print numbers from 0 to 1o using for


for h in range (11):
    print(h)

print('-------------------------------------')
    
#3. Stop the loop if the number = 5



for h in range (11):
    if h ==5:
        break
    print(h)

print('-------------------------------------')
    
#4. Skip the 5 iteration from print

for h in range (0,11):
    if h == 5:
        continue
    print(h)

print('-------------------------------------')


#5. Print multiplication table from 1 to 5

for x in range(1,6):
    print('-----------')
    for y in range (1,11):
        print(x,'*',y,'=',x*y)

print('-------------------------------------')
#6. How to get numbers from 10 to 20 using range

for i in range(10,21):
    print(i)
    
print('-------------------------------------')
# Generate numbers between 10 to 20

for i in range(10,20):
    print(i)

print ('----------------------')
#7. How to get numbers from 10 to 100 with 3 at each step using range

for i in range(10,100,3):
    print(i)

print ('----------------------')


#8. Get a list of even numbers from 1 to 100 using for



for x in range (2,100,2):
    print(x)


print('-------------------------------------')
#9. Get a list of even numbers from 1 to 100 using while

h=1
while h <=100:
    if h % 2 ==0:
        print(h)
    h +=1

print('-------------------------------------')
#10. Get a list of even numbers from 1 to 100 using range


for x in range (1,100):
    if x % 2 ==0:
        print(x)

print('-------------------------------------')

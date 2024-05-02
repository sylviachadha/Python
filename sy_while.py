# pgm1 - print numbers from 1 to 10 (can be 2500 as well)

num=1
while num<=10:
    print(num)
    num = num+1

# While doesn't have to do anything with
# incrementing number, u need to do
# that urself using a counter, it will
# only evaluate the condition in while
#-----------------------------------------------------------

# pgm2 - print only even numbers from 1 to 25

num=1
while num <= 25:
    if num%2 == 0:
        print(num)
    num = num + 1
#------------------------------------------------------------


# pgm3 - print only odd numbers from 1 to 25

num=1
while num <= 25:
    if num%2 != 0:
        print(num)
    num = num + 1
#-----------------------------------------------------------


# pgm4 - add only 4 names in a list.

name_list=[]
# means list will start from 0, so for 3 names it will be 0,1,2 hence < 3 in the condition

while len(name_list) < 3:
    name = input("Please enter a name: ")
    name_list.append(name)
print("Sorry list is full")
print(name_list)
#------------------------------------------------------------










# range
print(range(11))
# gives range iterable range(0,11)

# --------------------------------------------------

# for loop syntax
# for item in iterable:
    # Code to execute for each item
    # pass

# print numbers from 1 to 10

for i in range(11):    # using for with range iterable
    print(i)

# --------------------------------------------------

for i in [1,2,3,4]:     # using for with list iterable
    print(i)


# --------------------------------------------------

for letter in "India":    # using for with string iterable
    print(letter)

# --------------------------------------------------

for i in range(1,11,3):
    print(i)

# gives answer as 1, 4, 7 and 10

# --------------------------------------------------

# Count consonants and vowels in letter "Hello"

consonants = 0
con_list = []
vowels = 0
vowel_list = []

for letter in "Hello":
    if letter.lower() in 'aeiou':   # string is an iterable
        vowels = vowels + 1
        vowel_list.append(letter)
    elif letter==" ":
        pass
    else:
        consonants = consonants + 1
        con_list.append(letter)

print("There are {} vowels".format(vowels))
print(vowel_list)
print("There are {} consonants".format(consonants))
print(con_list)

# ---------------------------------------------------

# for loop with  a dictionary as an iterable

students = {
    "male" : ["Tom", "Charlie", "Harry", "Frank"],
    "female" : ["Sarah" , "Huda", "Samantha", "Emily","Elizabeth"]
    }


for name_list in students.values():
    for name in name_list:
        if 'a' in name:
            print(name)
        else:
            pass

# ---------------------------------------------------









  



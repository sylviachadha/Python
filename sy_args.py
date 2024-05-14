# Packing and Unpacking arguments
# ------------------------------

numbers = [1,2,3,4,5]
print(numbers)  # [1,2,3,4,5]

# 1. Unpack arguments - U can unpack any iterable data type before they go into functions
# ----------------------------------------------------------------------------

print(*numbers)  # 1 2 3 4 5
# This unpack results in 5 mini-arguments to
# function instead of 1 big list
# this unpack result is same as below-
print(1,2,3,4,5)   # 1 2 3 4 5

# string iterable data type normal version

print("abc")

# string iterable data type unpacked version

print(*"abc")       # a b c
# this unpack result is same as below-
print("a","b","c")   # a b c


# 2. Pack arguments - this works inside a function
# -----------------------------------------------
# Useful when u don't know how many arguments u r
# expecting & it makes ur function a lot more flexible


def add(x,y):
    return x + y

rzlt1 = add(10,10)
print(rzlt1)

# This is slightly limited cz this function has only 2 parameters
# so it won't work for 3,4,or 5 etc numbers so we pack
# numbers in the argument

# * operator in numbers makes it an iterable, specifically
# a tuple which allows u to pass variable number of
# arguments to the function & within function u can
# iterate over them as u would with any other iterable.

def add(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

rzlt2 = add(10,20,30,40)  # it works like tuple named numbers=(10,20,30,40)
print(rzlt2)



    



















# Function to add 2 numbers

# create a function
def add_numbers(x,y):
    return x+y

# call function
rzlt1 = add_numbers(2,3)
print(rzlt1)

# create a function to reverse an iterable e.g. string, list
def rev_str(text):
    text1 = text[::-1]
    return text1

# call function

rzlt2 = rev_str("pen")
print(rzlt2)

rzlt3 = rev_str([1,2,3,4])
print(rzlt3)


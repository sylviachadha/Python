# Create a variable called hello & store string/text in it

hello = "Hello World!"
print(hello)
print(type(hello))


# Project-------------

# Ask user for name, store user reply in a variable
name = input ("What is your name?: ")


# Ask user for age
age = input("What is your age?: ")


# Ask user for city
city = input("What is your city?: ")


# Ask user what they enjoy
love = input("What do you love doing?: ")


# Create output text, combine pieces of string together using string concatenation
text1 = "Your name is {}, you are {} years old. You live in {} and you love {}"
output1 = text1.format(name, age, city, love)


# Print output to screen
print(output1)






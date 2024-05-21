# Making an object using a class

# This class named as Pound has 6 states as below but no methods defined yet-
# Given some variables like value, color etc to represent object states

class Pound:
    
    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5   # mm
    thickness = 3.15  # mm
    heads = True

# Create an object from class Pound
coin1 = Pound()

# Access values
print(type(coin1))
print(coin1.value)
print(coin1.color)


# Change values
coin1.color = "greenish"
print(coin1.color)

# Create another object from class Pound
coin2 = Pound()
print(coin2.color)

# Each object is independent from other objects from the same class
# with its own unique characteristics

coin1.value = 1.25
print(coin1.value)
print(coin2.value)

# coin1 and coin2 came from exactly the same class but now as objects
# they behave independently









# Class methods (create behaviours for r coins)
# ---------------

# Making an object using a class. An object in object-oriented programming has states(attributes) and methods(behaviours).
#  __init__ and __del__ are constructor and destructor methods in a class.


import random
class Pound:

    def __init__(self, rare=False):

# __init__ Method is the Constructor method.
# It is called when an object is instantiated and is used to initialize the object's attributes (or state)
# It takes self (which represents the instance being created) as parameter. Can take more than 1 parameter.
# (self) is instance being created, if coin1 is created from Pound class, self is coin1.
# U don't type return inside ur constructor.

        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
            
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5   # mm
        self.thickness = 3.15  # mm
        self.heads = True

# Methods are defined within the class but not within the constructor.
# They are part of the class's definition and can use the attributes initialized by the constructor to
# perform actions or behaviors.

    def rust(self):  # self will be first parameter in class method
        self.color = "greenish"

    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


# __del__ Method is the Destructor method.
# A Destructor is called automatically when r program finishes & is used to destroy an object.
# It is called when an object is about to be destroyed.
# It is used to perform any necessary cleanup, such as closing files or releasing resources.

    def __del__(self):
        print("Coin Spent!")
        
        


# Creating objects from Pound class

coin1 = Pound(rare = True)  # coin1, object of class 
coin2 = Pound()                    # coin2, object of class

print(coin1.value)
print(coin2.value)

coin1.rust()
# Calling rust method of class pound, just like call append method of class list
# When you call the rust method on an instance of the Pound class, it modifies the state of the object.
# The rust method changes the color attribute of the Pound object to "greenish".
print(coin1.color)

coin1.clean()
print(coin1.color)

print(coin1.heads)
coin1.flip()
print(coin1.heads)

del coin1     # calling destructor

# coin1   this will give error as object coin1 is destroyed already

# Encapsulation
# --------------------

# Encapsulation in object-oriented programming ensures that:

# 1. Objects maintain their own state independently.
# 2. Internal states (set of attributes that hold data specific to that object) are hidden from each other and from external access.
# 3. Access to internal states is controlled through methods, preventing unauthorized or unintended modifications.
# (External Access refers to the ability to access an object's internal state (attributes) from outside the class itself.
# Encapsulation restricts this access, meaning that internal states are protected and can only be accessed or modified
# through the object's methods)


# The term "encapsulation" comes from the idea of "capsulating" or "wrapping" the data (attributes)
# and the code (methods) that operate on the data into a single unit, which we call an object.
# This bundling of data and methods into a single unit is the core idea of encapsulation.

# To sum up, encapsulation in OOP in Python is called so because it encapsulates or wraps the data
# and methods into a single unit, promotes data hiding, maintains object integrity, enhances modularity
# (creating self-contained objects. Each object can be developed, tested, and maintained independently
# of other objects) and improves code maintainability and reusability.

# Data hiding - restricting access to the internal state of an object, ensuring that data cannot be directly
# accessed or modified from outside the object.
# Modularity refers to the design principle of breaking down a software system into separate,
# self-contained units or modules, each responsible for a specific aspect of the system’s functionality.
# Modularity is often achieved through classes, functions, and packages that encapsulate specific
# functionality or components of a system.



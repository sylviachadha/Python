import random


# Base / Parent / Super class
# --------------------------

# Yes, the ** syntax in Python serves two purposes: it can both unpack a dictionary into keyword
# arguments and pack keyword arguments into a dictionary. This dual functionality makes it a
# powerful tool for handling flexible argument lists in functions and methods.
# The * operator in Python is used for packing and unpacking positional arguments, similar to how
# ** works for keyword arguments. This is particularly useful when you don't know beforehand all
# the attributes that might be needed.


class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **object_dict):
        
    # init or constructor class to initialize attributes of object
    # the explicit parameters are rare, clean, and heads **object_dict parameter is used to capture any
    # additional keyword arguments that are not explicitly listed
    # It collects these additional arguments into a dictionary named object_dict
    # object_dict will be a dictionary containing all the extra keyword arguments passed to the
    # Coin class init method which need to be initialized when the particular objects
    # (10 cents coin, pound coin) etc is instantiated, these contain attributes specific to those objects.
    # The important part is the ** syntax, which tells Python to collect any extra keyword arguments
    # into a dictionary. The name could be anything before **.

        for key, value in object_dict.items():
                setattr(self, key, value)

    # For each key-value pair in object_dict, setattr(self, key, value) sets an attribute/states on the self
    # object (the instance of the Coin class) with the name key and the value value.
    # e.g. self.thickness = 3.15 will be set using setattr
    
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color


    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):         # can be defined in any sequence but will be executed at end 
        print("Coin Spent")


    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


# Child / derived class
# ---------------------

# This Pound class will inherit from the parent/ base class which is Coin class.
# original_value, clean_color, rusty_color defined in the base class r values that 
# will be specific to a particular coin like 10 cents, 50 cents etc.

# Inside r child class init function we r going to get the parents init function/constructor
# to do the rest of the setup i.e. make methods cz only thing specific about each object is
# its data/attributes. The method can be taken from parent class.

# To run the parents init function we need to access the parent class, to do that we use
# Super function. super() and parent class are same.

class Pound(Coin):
    def __init__(self):
        data_dict = {"original_value" : 1.0,          # dictionary
                            "clean_color" : "gold",
                            "rusty_color" : "greenish",
                            "num_edges": 1,
                            "diameter" : 22.5,    
                            "thickness" : 3.15, 
                            "mass" : 9.5
                             }
    
        super().__init__(**data_dict) # access parent init class and pass this object specific data to it

                    # The **data syntax is used to unpack the dictionary data. This means that it converts the
                    # key-value pairs in the dictionary into keyword arguments when calling a function or
                    # method.
                    # The data dictionary is unpacked and passed to the Coin class's __init__ method using
                    # super().__init__(**data).

                    # Unpacking means-
                    # **data in super().__init__(**data) unpacks the data dictionary into keyword arguments.
                    # For example, if data is {"original_value": 1.0, "clean_color": "gold", "rusty_color":
                    # "greenish", "num_edges": 1, "diameter": 22.5, "thickness": 3.15, "mass": 9.5},
                    # unpacking it will result in original_value=1.0, clean_color="gold", rusty_color="greenish",
                    # num_edges=1, diameter=22.5, thickness=3.15, mass=9.5.
                    # These keyword arguments are then passed to the Coin class's __init__ method. 
        
                    # Process-
                    # In the Pound class, the data_dict dictionary is unpacked into individual keyword arguments
                    # using **data_dict.
                    # These unpacked keyword arguments are then passed to the Coin class's __init__ method.
                    # The __init__ method of the Coin class captures these additional keyword arguments using
                    # **object_dict, effectively converting them back into a dictionary named object_dict.
                    # It allows the __init__ method to accept and process an arbitrary number of keyword
                    # arguments without having to explicitly define them all.
                    # This is particularly useful when you don't know beforehand all the attributes that
                    # might be needed.
                    # So we r unpacking into keyword arguments here super()__init__(**data_dict) so
                    # that these keyword arguments can be passed to super class and we r packing into 
                    # dictionary here again in parent class Coin:
                    # def __init__(self, rare=False, clean=True, heads=True, **object_dict):
                    

# setattr
# -----------
# setattr does not take a dictionary as its argument. Instead, setattr takes three arguments:
# 1. The object on which you want to set the attribute.
# 2. The name of the attribute as a string.
# 3. The value you want to assign to the attribute.
# However, you can use a dictionary in combination with setattr to dynamically set multiple attributes
# on an object by iterating over the dictionary's items. 


#Instantiating object
#-------------------

# Only once an object is instantiated
one_pound_coin = Pound()

# After that its initial properties can be printed & then later also modified through methods

print(one_pound_coin.color)  # state after object instantiation
one_pound_coin.rust()           # call method
print(one_pound_coin.color)  # state of object changed after method called




        

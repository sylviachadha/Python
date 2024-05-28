import random


# Base / Parent / Super class
# --------------------------
class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **object_dict):

        for key, value in object_dict.items():
                setattr(self, key, value)
    
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


    def __str__(self):
        if self.original_value >= 1:
            return "€{} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))



# Child / derived class
# ---------------------

class One_Pence(Coin):
    def __init__(self):
        data_dict = {"original_value" : 0.01,          
                            "clean_color" : "bronze",
                            "rusty_color" : "brownish",
                            "num_edges": 1,
                            "diameter" : 20.3,    
                            "thickness" : 1.52, 
                            "mass" : 3.56,
                             }
    
        super().__init__(**data_dict)


class Two_Pence(Coin):
    def __init__(self):
        data_dict = {"original_value" : 0.02,          
                            "clean_color" : "bronze",
                            "rusty_color" : "brownish",
                            "num_edges": 1,
                            "diameter" : 25.9,    
                            "thickness" : 1.85, 
                            "mass" : 7.12,
                             }
    
        super().__init__(**data_dict)
        

class Five_Pence(Coin):
    def __init__(self):
        data_dict = {"original_value" : 0.05,          
                            "clean_color" : "silver",
                            "rusty_color" : None,
                            "num_edges": 1,
                            "diameter" : 18.0,    
                            "thickness" : 1.77, 
                            "mass" : 3.25,
                             }
    
        super().__init__(**data_dict)

# Cz silver coins don't rust we need to override standard behaviour
# that we r getting from r parent class

# The function is still with same name, its just gonna do something different

# Polymorphism - poly=multiple, morph=form
# U could override methods of parent class for some of the children classes,
# that's polymorphism.


    def rust(self):
        self.colour = self.clean_colour   # override std behaviour cz silver coins dont rust


class Ten_Pence(Coin):
    def __init__(self):
        data_dict = {"original_value" : 0.10,          
                            "clean_color" : "silver",
                            "rusty_color" : None,
                            "num_edges": 1,
                            "diameter" : 24.5,    
                            "thickness" : 1.85, 
                            "mass" : 6.50,
                             }
    
        super().__init__(**data_dict)

    def rust(self):
        self.colour = self.clean_colour   # override std behaviour cz silver coins dont rust


class Twenty_Pence(Coin):
    def __init__(self):
        data_dict = {"original_value" : 0.20,          
                            "clean_color" : "silver",
                            "rusty_color" : None,
                            "num_edges": 7,
                            "diameter" : 21.4,    
                            "thickness" : 1.7, 
                            "mass" : 5.00,
                             }
    
        super().__init__(**data_dict)

    def rust(self):
        self.colour = self.clean_colour   # override std behaviour cz silver coins dont rust


class Fifty_Pence(Coin):
    def __init__(self):
        data_dict = {"original_value" : 0.50,          
                            "clean_color" : "silver",
                            "rusty_color" : None,
                            "num_edges": 7,
                            "diameter" : 27.3,    
                            "thickness" : 1.78, 
                            "mass" : 8.00,
                             }
    
        super().__init__(**data_dict)

    def rust(self):
        self.colour = self.clean_colour   # override std behaviour cz silver coins dont rust


class One_Pound(Coin):
    def __init__(self):
        data_dict = {"original_value" : 1.0,          
                            "clean_color" : "gold",
                            "rusty_color" : "greenish",
                            "num_edges": 1,
                            "diameter" : 22.5,    
                            "thickness" : 3.15, 
                            "mass" : 9.5
                             }
    
        super().__init__(**data_dict)


class Two_Pound(Coin):
    def __init__(self):
        data_dict = {"original_value" : 2.0,          
                            "clean_color" : "gold & silver",
                            "rusty_color" : "greenish",
                            "num_edges": 1,
                            "diameter" : 28.4,    
                            "thickness" : 2.50, 
                            "mass" : 12.00
                             }
    
        super().__init__(**data_dict)


coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(), Fifty_Pence(),
              One_Pound(), Two_Pound()]

for coin in coins:
    args = [coin, coin.color, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]

    string = "{}- colour: {}, value:{}, diameter:{}, thickness:{}, num_edges:{}, mass:{}".format(*args)
    # unpack- *args
    print(string)








        

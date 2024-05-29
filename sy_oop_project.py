# Parent classes are used when there is a need to create a class hierarchy where the parent class provides
# a common interface and potentially some default behavior that child classes can inherit and/or override.

# A parent class is a regular class that can be instantiated and can have its own methods and properties.
# Other classes can inherit from it to reuse its code and extend its functionality. Instances of a parent class
# can be created directly.

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance = self.balance + amount


    def withdraw(self, amount):
        if self.balance - amount >=self.min_balance:
            self.balance = self.balance - amount
        else:
            print("Sorry, not enough funds")


    def statement (self):
        print("Account Balance: €{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

# string method
    def __str__(self):
       return "{}'s Current Account: Balance €{}".format(self.name, self.balance)

        
x = Current('Emily', 500)
x.deposit(300)
x.statement()
x.withdraw(1000)
x.statement()
x.withdraw(800)
x.statement()
x.withdraw(1)

# When printing object-

print(x)

# Without __str__ Method: Python prints the default string representation, which includes the class name
# and memory address.
# With __str__ Method: Python prints the string returned by the __str__ method, which can be customized
# to provide a more informative and user-friendly representation of the object.


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
    def __str__(self):
       return "{}'s Savings Account: Balance €{}".format(self.name, self.balance)


y = Savings("Tom", 300)
print(y)
y.deposit(200)
y.statement()
y.withdraw(500)
y.statement()
y.withdraw(1)
        
        
        

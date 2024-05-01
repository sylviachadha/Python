# 1. NOT logical Operator

x = 10
y = 20

if not y < x:
    print("this is not operator")

# 2. AND logical Operator

a = 4
b = 8
if a > b and b >= 8:
    print("this is and operator")


# 3. NAND Operator
# As per BODMAS inside brackets will be executed first

if not (a > b and b >= 8):
    print("this is nand operator")

    
if not a < b and b >= 8:
    print("this is without bracket")


# 4. OR Operator

c = 5
d = -1

if c > 1 or d >1:
    print("this is or operator")

d = 5

if c >1 or d > 1:
    print("this is or operator")


if c>500 or d>200:
    print("this is or operator")


# 5. NOR Operator

if not (c>500 or d>200):
    print("this is nor operator")


# Mixed

c = 6
d = 2

if (c>5 and d>5) or (c>1 and d>1):
    print("it worked")


if not ((c>5 and d>5) or (c>1 and d>1)):
    print("it didn't worked")
    







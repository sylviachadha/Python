# 1. GLOBAL SCOPE
# -------------------------

a = 100

def f1():
    print(a)

def f2():
    print(a)


# call function
f1()
f2()

# since a has global scope it is
# visible inside both f1 and f2
# as global variables can be seen
# anywhere in the program


# 2. LOCAL SCOPE
# -------------------------


def f3():
    n = 50
    print(n)

def f4():
    print(n)

# call function
f3()
#f4()

# now here since n is defined inside
# f3 local scope so when u call these
# functions f3 displays value of n
# while f4 throws error cz that variable
# is not visible to f4 cz it is inside local
# scope of f3


# 3. LOCAL SCOPE
# -------------------------


# Even though same variable name used but
# they r still treated different variables cz they are
# inside different functions & each function
# has its own local scope.

def f5():
    b = 100
    print(b)

def f6():
    b = 50
    print(b)

# call function
f5()
f6()


# 4. GLOBAL SCOPE AND LOCAL SCOPE
# -----------------------------------


a = 250   # global variable

def f7():
    a = 50  # when u try to change a global variable from inside a local
    print(a) # scope python stops that from happening & automatically
                # creates a local variable with the same name 

def f8():
    a = 100
    print(a)

f7()     # 50
f8()     # 100
print(a)  # 250


# 5. GLOBAL SCOPE AND LOCAL SCOPE
# ------------------------------------


a = 250

def f9():
    b = a + 10
    print(b)
# inside its local scope it could not find
# variable a, so it looked outside into the
# the global scope and use that global value

def f10():
    a = 50
    print(a)
# in this case python will not let overwrite a
# global variable but just create a local
# variable & print that

f9()
f10()
print(a)
# cz global variable is protected it still has its
# original value of 250




# 6. CHANGING GLOBAL VARIABLE FROM WITHIN  A FUNCTION
# ---------------------------------------------------

a = 250

def f11():
    global a
    a = 100   # global
    print(a)

def f12():
    a = 50     # local
    print(a)

f11()
f12()
print(a)


# 7. FOR LIST/DICTIONARY GLOBAL KEYWORD NOT REQUIRED
#     IF ONLY A PART OF LIST/DICT IS CHANGED
# ---------------------------------------------------

a =[1,2,3]

def f13():
    a[0]=5
    print(a)


def f14():
    a = 50
    print(a)


f13()     # [5,2,3]
f14()     # 50
print(a) # [5,2,3]



# 8. IF WHOLE LIST/DICTIONARY CHANGEED AGAIN GLOBAL
#     KEYWORD IS REQUIRED
# ---------------------------------------------------

a =[1,2,3]

def f13():
    global a
    a=[5,6,7]
    print(a)


def f14():
    a = 50
    print(a)


f13()     # [5,6,7]
f14()     # 50
print(a) # [5,6,7]









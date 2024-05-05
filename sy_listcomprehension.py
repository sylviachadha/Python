# List comprehension : Returns a new list based on an expression and condition
# Syntax
# [expression for item in iterable if condition]


# If returns a list it is list comprehension, if returns a dictionary it is Dictionary Comprehension
# If returns a set it is set comprehension. However iterables in any of comprehensions can be any
# iterable like list, tuple, dictionary,ranges etc. The name is based on what it returns as output.

#-----------------------------------------------------------------------------


# A list comprehension on numbers-

even_num = [x for x in range(1,101) if x%2 == 0]
print(even_num)

# A list comprehension that squares all even numbers from 0 to 9:

square_num = [x**2 for x in range(0,10) if x%2 == 0]
print(square_num)

#-----------------------------------------------------------------------------

# A list comprehension on strings-

words = ["the","quick", "brown","fox"]
word_list = [[w.lower(), w.upper(), len(w)] for w in words]
print(word_list)

# [['the', 'THE', 3], ['quick', 'QUICK', 5], ['brown', 'BROWN', 5], ['fox', 'FOX', 3]]


#-----------------------------------------------------------------------------








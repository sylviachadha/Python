import random

health = 50

difficulty = 3

# Casting 
potion_health = int(random.randint(25,50) / difficulty)

# Can overwrite variable health
health = health + potion_health

print(health)

 



# pgm1 - ask a question and only stop once the answer begins with "just because"

answer = input("Why is the sky blue? ")

while answer!= "just because":
    # u need to store new ans every 1   time u ask "Why"
    answer = input("Why? ")
    
print("You answered right!")


# pgm2 - Make a list of questions & select any 1 randomly
# and only stop once the answer begins with "just because"

import random

questions = ["Why is the sky blue?", "Why is there face on moon?", "Where r all the dinosaurs?"]

question = random.choice(questions)
answer = input(question)
while answer!= "just because":
    # u need to store new ans every 1   time u ask "Why"
    answer = input("Why? ")
    
print("You answered right!")

    

import random

def say_something(names):
    greetings = ['Hey', 'Hello', 'Hi', 'Good Afternoon', 'Good morning'] 

    name = random.choice(names)

    greeting = random.choice(greetings)
    print(f'{greeting}, {name}!')

say_something(["Sam", "Naeem", "Kassidy"])
#def catchingUp():
  #  print("How have ")



#chitchat = [catchingUp, salutations, say_something]


import random

pets = ["Cat", "Dog", "Sloth", "Moose"]
print(pets)

# Grab a random item from list
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))
        # use random.choice() instead of pets[random.randint(0, len(pets) - 1)]  . Much cleaner.

# Randomize order of list. Mutates original, does Not make a copy.
random.shuffle(pets)
print(pets)
random.shuffle(pets)
print(pets)

 
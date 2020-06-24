import random, sys

print("I am thinking of a number between 1 and 20.")
answer = random.randint(1, 20)
for i in range(20):
    # user is prompted to guess
    guess = round(float(input("Take a guess. Only whole numbers please!\n")))
    if guess == answer:
        print("Good Job! You guessed my number in " + str(i+1) + " guesses!")
        print("Toodle-oo!")
        sys.exit()
    elif guess < answer:
        print("Your guess is too low.")
    else:   # if guess is not correct, and is not too low, it must be too high
        print("Your guess is too high.")
print("You did something very difficult to do. You guessed 20 times, but never guessed correctly!  Better luck next time.")
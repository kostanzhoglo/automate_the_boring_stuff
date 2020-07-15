import random
numberOfStreaks = 50

def coinFlip():
    totalTails = 0
    for flip in range(100):
        # Code that creates a list of 100 'heads' or 'tails' values
        if random.randint(0, 1) == 0:
            totalTails += 1
            print('T', end='')
        else:
            print('H', end='')
        if flip == 99:
            print()
    print("Tails came up " + str(totalTails) + "x.")
    print("Heads came up " + str(100 - totalTails) + "x.")

    

coinFlip()


print('Chance of streak: %s%%' % (numberOfStreaks / 100))
# print("%% %")

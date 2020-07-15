import random
numberOfStreaks = 0
experiment_reps = 0

while experiment_reps < 10000:
    flip_results = []

    for flip in range(100):
        if random.randint(0, 1) == 0:
            flip_results.append("T")
        else:
            flip_results.append("H")

    # This will find streaks of T or H.  
    for i in range(len(flip_results)):
        in_a_row = 0
        for j in range(6):
            try: 
                if flip_results[i] == flip_results[i + j]:
                    in_a_row += 1
                else:
                    break
            except IndexError:
                break

        if in_a_row == 6:
            numberOfStreaks += 1

    experiment_reps += 1

print(f"Streak of 6 in a row: {str(numberOfStreaks)}")
print(f"Total Coin Flips: {str((experiment_reps) * 100)}")
print(f"The odds of getting 6 Tails or 6 Heads in a row is: {str((numberOfStreaks / 10000))}")

# def coinFlip():
#     totalTails = 0
#     flip_results = ''
#     for flip in range(100):
#         # Code that creates a list of 100 'heads' or 'tails' values
#         if random.randint(0, 1) == 0:
#             totalTails += 1
#             flip_results += 'T'
#         else:
#             flip_results += 'H'
#         if flip == 99:
#             print()
#     print(flip_results)
#     print("Tails came up " + str(totalTails) + "x.")
#     print("Heads came up " + str(100 - totalTails) + "x.")

# coinFlip()



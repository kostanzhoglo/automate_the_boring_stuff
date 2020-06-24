import random, sys

print("Welcome to... \nROCK, PAPER, SCISSOR")

user_wins = 0
user_losses = 0
user_ties = 0

print(f"{user_wins} Wins, {user_losses} Losses, {user_ties} Ties")


user_choice = ''
while user_choice != 'q':
    game_options = ['r', 'p', 's']
    computer_choice = random.choice(game_options)
    user_choice = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit:\n")
    if user_choice == 'q':
        sys.exit()
    elif user_choice == 'r' and computer_choice == 'r':
        print(user_choice)
        print("ROCK vs. ...")
        print("ROCK\nIt is a tie!")
        user_ties += 1
        print(f"{user_wins} Wins, {user_losses} Losses, {user_ties} Ties")
        continue
    elif user_choice == 'r' and computer_choice == 'p':
        
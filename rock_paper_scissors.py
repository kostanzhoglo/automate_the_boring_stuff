import random, sys

print("Welcome to... \nROCK, PAPER, SCISSOR")

user_wins = 0
user_losses = 0
user_ties = 0

def show_user_choice(user_choice):
    # print(user_choice)
    if user_choice == 'q':
        sys.exit()
    elif user_choice == 'r':
        print('ROCK versus...')
    elif user_choice == 'p':
        print('PAPER versus...')
    else:
        print('SCISSORS versus...')

def show_computer_choice(comp_choice):
    if comp_choice == 'r':
        print('ROCK')
    elif comp_choice == 'p':
        print('PAPER')
    else:
        print('SCISSORS')





user_choice = ''
while user_choice != 'q':
    game_options = ['r', 'p', 's']
    comp_choice = random.choice(game_options)

    print(f"{user_wins} Wins, {user_losses} Losses, {user_ties} Ties")
    user_choice = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit:\n")
    
    show_user_choice(user_choice)
    show_computer_choice(comp_choice)

    if user_choice == comp_choice:
        print("It's a tie!")
        user_ties = user_ties + 1
    elif (user_choice == 'r' and comp_choice == 's') or (user_choice == 's' and comp_choice == 'p') or (user_choice == 'p' and comp_choice == 'r'):
        print("You win!")
        user_wins = user_wins + 1
    elif (user_choice == 'r' and comp_choice == 'p') or (user_choice == 's' and comp_choice == 'r') or (user_choice == 'p' and comp_choice == 's'):
        print("You lose!")
        user_losses = user_losses + 1

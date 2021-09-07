import random

choices = ['r','p','s']

choices_meaning = {
    'r' : 'Rock',
    's' : 'Scissors',
    'p' : 'Paper'
}

user_choice = input('Select from Rock, Paper, Scissors: (r, p, s) ')

ai_choice = random.choice(choices)

if user_choice in choices:
    print(f'Your choice is {choices_meaning[user_choice]}. AI choice is {choices_meaning[ai_choice]}.')
    # r > s - p > r - s > p
    if user_choice == ai_choice:
        print('Tie')
    elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r')  or (user_choice == 's' and ai_choice == 'p'):
        print("You Won!")
    else:
        print('You Lost!')
else:
    print('Invalid input')
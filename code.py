import random

choices = ['r','p','s']

choice_meaning = {
    'r' : 'Rock',
    's' : 'Scissors',
    'p' : 'Paper'
}

user_score = 0
ai_score = 0 
final_number = 5

while True:
    user_choice = input('Select from Rock, Paper, Scissors: (r, p, s) ')
  
    ai_choice = random.choice(choices)

    if user_choice in choices:
        print(f'Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
        # r > s - p > r - s > p
        if user_choice == ai_choice:
            print('Tie')
        elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r')  or (user_choice == 's' and ai_choice == 'p'):
            print("user+1!")
            user_score += 1
        else:
            print('AI+1!')
            ai_score += 1
    else:
        print('Invalid input') 

    print(f'User Score: {user_score} / AI Score: {ai_score}')

    if user_score == final_number or ai_score == final_number:
        break

    print('\n','-'*15,'\n') 

if user_score == final_number: 
    print(f'User won with Score: {user_score}')
else :
    print(f'AI won with Score: {ai_score}') 
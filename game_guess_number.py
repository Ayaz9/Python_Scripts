# Game should be played between 2 people, one of them enters the number and the other one guesses it

import random, os
print('''Game started !
Please enter your number and ask your friend to find it :''')
while True:
    try:
        user_input = int(input())
        break
    except :
        print('Please enter integer value')
os.system('clear')  # clear input for MAC
generated_number = random.randint(5,500)
i = 1
if user_input > 0:
    print(type(user_input))
    print(type(generated_number))
    print(f'Please guess the number, it is between 0 and {user_input+generated_number}. You have 10 chances to find it :')
    # print('Please guess the number, it is between 0 and '+str(user_input+generated_number)+' you will have 10 chances to find it :')
if user_input <= 0:
    print(f'Please guess the number, it is between 0 and {user_input-generated_number}. You have 10 chances to find it :')
    # print('Please guess the number, it is between 0 and '+str(user_input-generated_number)+' you will have 10 chances to find it :')
while i<=10:
    guessed_number=int(input())
    if guessed_number != user_input and i == 10:
        print('Please contact with administrator')
    elif guessed_number > user_input:
        print(f'Lower, {10-i} chances left')
    elif guessed_number < user_input:
        print(f'Higer, {10-i} chances left')
    else:
        print(f'Congratulations! In {i} attempts you found it, it was {guessed_number}')
        break
    i += 1
input('Press enter to close the program')


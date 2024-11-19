import random

secret_number = random.randint(1, 100)
attempts = 0
wrong_input = 0

while attempts != 10:
    try:
        user_number = int(input(f'Guess the number ({10 - attempts} attempts left): '))

        if user_number == secret_number:
            print('You guessed it right!')
            break
        elif user_number <= secret_number:
            print('Too low, the secret number is above that')
        elif user_number == (secret_number - 1) or user_number == (secret_number + 1):
            print('Too close')
        elif user_number >= secret_number:
            print('Too high, the secret number is below that')
        else:
            print('Try again')

        attempts += 1

        if attempts == 10:
            print('But you ran out of chances')
            print('Secret number was', secret_number)
            break
    except ValueError:
        if wrong_input == 3:
            print('You entered too many wrong inputs, program is exiting')
            break
        print('Enter only numerical')
        wrong_input += 1
        continue
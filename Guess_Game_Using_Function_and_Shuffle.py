from random import shuffle


def shuffle_list(list):
    shuffle(list)
    return list


def player_guess():
    guess_number = ''
    while guess_number not in ['0', '1', '2']:
        guess_number = input('Guess the number: ')
    return int(guess_number)


def check_guess(saved_number, guess):
    if saved_number[guess] == '0':
        print('Correct Guess')
    else:
        print('You are wrong')
        print(f'Correct Answer: {saved_number}')


saved_number = ['', '0', '']
shuffled_list = shuffle_list(saved_number)
guess = player_guess()
check_guess(shuffled_list, guess)

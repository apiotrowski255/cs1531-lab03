'''
Number Guessing Game.

Guesses are made until all numbers are guessed.
The game reveals whether the closest unguessed number is higher or lower than each guess.
Numbers are distinct.
Typing 'q' quits the game.
'''

import random

MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present.
    # copy = list(values)
    if guess in values:
        index = values.index(guess)
        del values[index]
    else:
        find_closest(guess, values)
    return values
    '''
    try :
        index = values.index(guess)
        del values[index]
        return values
        #return copy
    except:
        find_closest(guess, values)
        return values
    '''
    # critics from myself, my function does not return a duplicate list
    # because it would be much faster to edit the values in place
    # rather than creating a new list and then reassigning it to values

def find_closest(guess, values):
    # This function should return the closest value
    # to the guessed value.
    copy = list(values)
    copy.append(guess)
    copy= sorted(copy)
    index = copy.index(guess)
    if index == 0 or index == len(copy) - 1:
        if index == 0:
            print('higher')
            return copy[1]
        else:
            print('lower')
            return copy[-2]
    else:
        lower = copy[index - 1]
        higher = copy[index + 1]
        if higher - guess <= guess - lower:
            print('higher')
            return higher
        else:
            print('lower')
            return lower

def run_game(values):
    # While there are values to be guessed and the user hasn't
    # quit (with 'q'), the game should wait for the user to input
    # their guess and then reveal whether the closest number is
    # lower or higher.
    print(f'Numbers are between {MIN} and {MAX} inclusive. There are {len(values)} values left.')
    guess = input('There are {} values left. Guess: '.format(len(values)))
    # Your code goes here.
    while True:
        if guess == 'q' or values == []:
            break
        guess = int(guess)
        print(guess)
        values = handle_guess(guess, values)
        #print(values)
        if values == []:
            print("Congratulations! You won!")
            break
        guess = input('There are {} values left. Guess: '.format(len(values)))

    print('Thanks for playing! See you soon.')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    #print(values)
    run_game(values)

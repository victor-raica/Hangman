import random
import re


def hide_chars(string, letters_to_reveal_set):
    return ''.join((char if char in letters_to_reveal_set else '-' for char in string))


def play():
    word_list = ['python', 'java', 'swift', 'javascript']
    word_to_guess = random.choice(word_list)
    attempts = 8
    revealed_letters = set()
    wrong_guesses = set()
    lost_condition = False
    won_condition = False
    while not (lost_condition or won_condition):
        print()
        print(hide_chars(word_to_guess, revealed_letters))
        letter = input('Input a letter: ')
        if not len(letter) == 1:
            print('Please, input a single letter.')
        elif not re.search(r'[a-z]', letter):
            print('Please, enter a lowercase letter from the English alphabet.')
        elif letter in wrong_guesses or letter in revealed_letters:
            print("You've already guessed this letter.")
        elif letter not in word_to_guess:
            print("That letter doesn't appear in the word.")
            wrong_guesses.add(letter)
            attempts -= 1
        elif letter in revealed_letters:
            print('No improvements')
            attempts -= 1
        else:
            revealed_letters.add(letter)
        lost_condition = attempts == 0
        won_condition = '-' not in hide_chars(word_to_guess, revealed_letters)
    if won_condition:
        print()
        print(word_to_guess)
        print(f'You guessed the word {word_to_guess}!')
        print('You survived!')
        return True
    else:
        print()
        print('You lost!')
        return False


wins = 0
losses = 0
menu_choice = 'play'
print('H A N G M A N')
while menu_choice != 'exit':
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    menu_choice = input()
    if menu_choice == 'play':
        won = play()
        if won:
            wins += 1
        else:
            losses += 1
    elif menu_choice == 'results':
        print(f'You won: {wins} times.')
        print(f'You lost: {losses} times.')

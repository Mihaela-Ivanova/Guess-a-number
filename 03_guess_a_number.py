import random

computer_number = random.randint(1, 100)
player_choice = 0

while True:
    player_input = input('Try to guess the number that the computer has picked between 1 - 100: ')
    if not player_input.isdigit():
        print('Invalid choice. Please try again.')
        continue

    player_choice = int(player_input)

    if player_choice == computer_number:
        print('You guessed right! Congratulations!')
        break

    elif player_choice > computer_number:
        print("Guess is too high!")

    else:
        print("Guess is too low!")
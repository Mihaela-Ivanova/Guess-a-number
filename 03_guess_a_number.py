import random

final_range = 100

while True:
    computer_number = random.randint(1,final_range)
    tries = 0

    while True:
        player_input = input(f'Try to guess the number that the computer has picked between 1 - {final_range}: ')
        if not player_input.isdigit():
            print('Invalid choice. Please try again.')
            continue

        player_choice = int(player_input)

        if player_choice == computer_number:
            print('You guessed right! Congratulations!')
            final_range += 100
            tries = 0
            break

        elif player_choice > computer_number:
            print("Guess is too high!")

        else:
            print("Guess is too low!")

        tries += 1

        if tries == 8:
            print("Sorry! You tried to guess 8 times and didn't guess the number")
            break

    a = input("Do you want to play again? (y/n): ")
    while a != 'y' or a != 'n':
        if a == 'y':
            print(f"The computer has picked a new number. The number will be between 1 and {final_range}. Try to guess it.")
            break
        elif a == 'n':
            print("Good game!")
            exit()
        else:
            a = input("Invalid choice\nPick (y/n): ")

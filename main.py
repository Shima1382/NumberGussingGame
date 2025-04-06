from random import randint
from math import log2

class Game():
    @staticmethod
    def get_valid_input(prompt, input_type, valid_range=None, allow_empty=False):
        while True:
            user_input = input(prompt).strip()
            # barresie meghdaare khaali
            if allow_empty and user_input == '':
                return None
            try:
                # voroodi ro be type morede nazar tabdil mikonim
                user_input = input_type(user_input)
                if valid_range and user_input not in valid_range:
                    print(f'input must be between {valid_range}')
                return user_input
            except ValueError as e:
                print('invalid input,please enter valid input')

    @staticmethod
    def game_management():
        print("Hello,you are welcome to Guess the Number Game!")
        while True:
            min_number = Game.get_valid_input("Enter minimum number: ", int)
            max_number = Game.get_valid_input("Enter maximum number: ", int)
            if max_number <= min_number:
                print("Maximum number must be greater than minimum number")
                break

            random_number = randint(min_number,max_number)
            max_number_of_guess = round(log2(max_number - min_number + 1))
            print(f"you have {max_number_of_guess} chances to guess the number.Start now")

            number_of_guess = 0
            while number_of_guess < max_number_of_guess:
                guessed_number = Game.get_valid_input("Enter your guessed number: ", int)
                number_of_guess += 1
                if random_number > guessed_number:
                    print("your guessed number is smaller than the random number")
                elif random_number < guessed_number:
                    print("your guessed number is greater than the random number")
                else:
                    print(f'Congrats! You guessed the number!you found it in {number_of_guess} attempt!')
                    break
            else:
                print(f"your chance has finished")

            while True:
                last_answer = Game.get_valid_input("Do you want to play again?(y/n): ", str)
                if last_answer in ["y", "n"]:
                    break
                print("invalid input,please enter y or n")
            if last_answer.lower() != 'y':
                print("Thank you for playing")
                break

play_game = Game()
play_game.game_management()
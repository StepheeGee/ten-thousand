# ten_thousand/play_game.pypython3 -m ten_thousand.play_game

from ten_thousand.game_logic import GameLogic
from re import search

class PlayGame:
    def __init__(self, roller=GameLogic.roll_dice):
        self.roller = roller
        self.banked_score = 0
        self.round_num = 0
        self.max_rounds = 20
     
        
    def start_game(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        while True:
            play_or_not = input("> ").lower()
            if play_or_not == "y":
                return True
            elif play_or_not == "n":
                print("OK. Maybe another time")
                return False
            else:
                print('Please type "y" or "n"')

    def play_game(self, num_dice=None):
        while self.banked_score < 10000 and self.round_num < self.max_rounds:
            result = self.play_round(num_dice)
            if result is False:
                print(f"Thanks for playing. You earned {self.banked_score} points")
                return
            else:
                self.round_num, shelf_score = result[0:2]
                self.banked_score += shelf_score
                print(f"You banked {shelf_score} points in round {self.round_num}\nTotal score is {self.banked_score} points")

        if self.banked_score >= 10000:
            print(f"Congratulations!! You have won with {self.banked_score} points in {self.round_num} rounds!")
        else:
            print(f"You failed to reach 10,000 in {self.max_rounds}. You scored {self.banked_score}. Better luck next time!")
    

    def play_round(self, num_dice):
        dice_remaining = 6
        shelf_score = 0
        while True:
            self.rolling_message(shelf_score)
            rolled_dice = self.roll_dice(dice_remaining, num_dice)
            selection_result = self.select_score_compare(rolled_dice)
            if selection_result is False:
                return False
            selected_dice, roll_score, scoring_dice = selection_result
            if roll_score == 0:
                self.print_zilch()
                return self.round_num + 1, 0
            shelf_score += roll_score
            dice_remaining -= len(scoring_dice)
            if dice_remaining == 0:
                dice_remaining = 6
            print(f"You have {shelf_score} unbanked points and {dice_remaining} dice remaining")
            user_choice = self.bank_roll_or_quit()
            if user_choice is False:
                return False
            elif user_choice is True:
                return self.round_num + 1, shelf_score

    def select_score_compare(self, rolled_dice):
        possible_scorers = GameLogic.get_scorers(rolled_dice)
        if len(possible_scorers) > 0:
            selection_result = self.select_and_score(rolled_dice)
            if selection_result is False:
                return False
            selected_dice, roll_score, scoring_dice = selection_result
            while len(selected_dice) != len(scoring_dice):
                differences = self.find_difference(selected_dice, scoring_dice)
                print("Cannot shelf the following dice as they are non-scoring")
                print("*** " + ' '.join([str(num) for num in differences]) + " ***")
                print("Please choose again")
                selection_result = self.select_and_score(rolled_dice)
                if selection_result is False:
                    return False
                selected_dice, roll_score, scoring_dice = selection_result
            return selected_dice, roll_score, scoring_dice
        else:
            return [], 0, []

    def select_and_score(self, rolled_dice):
        selected_dice = self.select_dice(rolled_dice)
        if selected_dice is False:
            return False
        scoring_dice = GameLogic.get_scorers(selected_dice)
        roll_score = GameLogic.calculate_score(scoring_dice)
        return selected_dice, roll_score, scoring_dice

    def rolling_message(self, shelf_score):
        if shelf_score == 0:
            print(f"Starting round {self.round_num + 1}")
        print(f"Rolling 6 dice...")

    def roll_dice(self, dice_remaining, num_dice=None):
        rolled_dice = self.roller(dice_remaining) if num_dice is None else num_dice
        print("*** " + ' '.join([str(num) for num in rolled_dice]) + " ***")
        return rolled_dice

    def print_zilch(self):
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

    def select_dice(self, rolled_dice):
        while True:
            print("Enter dice to keep, or (q)uit:")
            user_input = input("> ").lower()
            user_input = user_input.replace(" ", "")
            if user_input == "q":
                return False
            if user_input == "":
                return []

            if search(r"[^1-6]", user_input) or len(user_input) > len(rolled_dice):
                print('You may enter "q" or numbers between 1-6 of the same amount or less than the number of rolled dice')
                continue
            selected_dice = [int(char) for char in user_input]
            if GameLogic.validate_keepers(rolled_dice, selected_dice):
                return selected_dice
            else:
                print("Cheater!!! Or possibly made a typo...")
                print("*** " + ' '.join([str(num) for num in rolled_dice]) + " ***")
                continue



    def find_difference(self, selected_dice, scoring_dice):
        non_scoring_dice = [die for die in selected_dice if die not in scoring_dice]
        if non_scoring_dice:
            print("Non-scoring dice: ", non_scoring_dice)
        else:
            print("Cannot shelf the following dice as they are non-scoring")
        return non_scoring_dice



    def bank_roll_or_quit(self):
        while True:
            print("(r)oll again, (b)ank your points or (q)uit:")
            user_input = input("> ").lower()
            if user_input == "q":
                return False
            elif user_input == "b":
                return True
            elif user_input == "r":
                return
            else:
                print('please type "r" to roll again, "b" to bank your points, or "q" to quit:')


def play(roller=None):
    game_instance = PlayGame(roller=roller)
    if game_instance.start_game():
        game_instance.play_game()

if __name__ == "__main__":
    game_instance = PlayGame()


    if game_instance.start_game():
        game_instance.play_game()





# class PlayGame:
#     def __init__(self, roller=None):
#         print("Welcome to Ten Thousand!\n(y)es to play or (n)o to decline")
#         play_game = input("> ").lower()
#         if play_game == "n":
#             print("OK. Maybe another time.")
#             exit()

#         print("Starting round 1")
#         self.banker = Banker()
#         self.current_round = 1
#         self.roller = roller

#     def play(self):
#         while True:
#             self.play_round()
#             if not self.should_continue():
#                 break

#     def play_round(self):
#         num_dice = 6
#         self.current_round += 1
#         while True:
#             print(f"\nRound {self.current_round}")
#             initial_roll = self.roller(num_dice) if self.roller else GameLogic.roll_dice(num_dice)
#             print(f"Rolling {num_dice} dice...\n*** {' '.join(map(str, initial_roll))} ***")

#             while True:
#                 user_input = input("Enter dice to keep, or (q)uit: ")
#                 user_dice = self.parse_user_input(user_input, initial_roll)

#                 if user_dice is None:
#                     print("Cheater!!! Or possibly made a typo...")
#                     print(f"*** {' '.join(map(str, initial_roll))} ***")
#                 else:
#                     break

#             score = GameLogic.calculate_score(user_dice)
#             print(f"You have {score} unbanked points and {num_dice - len(user_dice)} dice remaining")


#             choice = input("Do you want to (B)ank your score, (R)oll again, or (Q)uit? ").upper()

#             if choice == 'B':
#                 self.banker.shelf(score)
#                 self.banker.bank()
#                 print(f"\nYou banked {self.banker.shelved} points in round {self.current_round}")
#                 print(f"Total score is {self.banker.balance} points")
#                 self.current_round += 1
#                 break
#             elif choice == 'R':
#                 num_dice -= len(user_dice)
#                 new_roll = self.roller(num_dice) if self.roller else GameLogic.roll_dice(num_dice)
#                 print(f"\nRolling {num_dice} dice...\n*** {' '.join(map(str, new_roll))} ***")
#             elif choice == 'Q':
#                 print("Thanks for playing! Final score:", self.banker.balance)
#                 exit()

#     def parse_user_input(self, user_input, initial_roll):
#         try:
#             user_dice = list(map(int, user_input.split()))
#             if not all(die in initial_roll for die in user_dice):
#                 return None
#             return user_dice
#         except ValueError:
#             return None





#     def roll_again(self, num_dice, num_to_set_aside):
#         if num_to_set_aside < num_dice:
#             set_aside_dice = set(input("Enter dice to set aside:\n> "))
#             current_roll = tuple(die for die in self.roller(num_dice) if die not in set_aside_dice) \
#                 if self.roller else tuple(die for die in GameLogic.roll_dice(num_dice) if die not in set_aside_dice)
#             self.update_score(current_roll)
#         else:
#             print("Invalid input. You can't set aside more dice than you have.")

#     def update_score(self, current_roll):
#         score = GameLogic.calculate_score(current_roll)
#         print(f"\nYour new roll: {current_roll}")
#         print(f"Score for this roll: {score}")
#         if score == 0:
#             print("\n****************************************")
#             print("**        Zilch!!! Round over         **")
#             print("****************************************")
#             self.banker.clear_shelved()
#         else:
#             self.play_round()

#     def should_continue(self):
#         if self.banker.shelved > 0:
#             choice = input("Do you want to (C)ontinue or (Q)uit?\n> ").upper()
#             return choice == 'C'
#         else:
#             return True


# class Banker:
#     def __init__(self):
#         self.balance = 0
#         self.shelved = 0

#     def shelf(self, points):
#         self.shelved += points

#     def clear_shelved(self):
#         self.shelved = 0

#     def bank(self):
#         self.balance += self.shelved
#         self.clear_shelved()


# if __name__ == "__main__":
#     game = PlayGame(roller=GameLogic.roll_dice)
#     game.play()


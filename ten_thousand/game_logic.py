import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll.

        :param dice_roll: Tuple of integers representing the dice roll.
        :return: Integer representing the roll's score.
        """
        # Check for a straight from 1 to 6, return 1500 if true
        if set(dice_roll) == set(range(1, 7)):
            return 1500
        # Check for three pairs, return 1500 if true
        if len(dice_roll) == 6 and all(dice_roll.count(value) == 2 for value in set(dice_roll)):
            return 1500

        # Initialize score to 0
        score = 0
        # Count occurrences of each number in the dice roll and create a dictionary
        counts = {x: dice_roll.count(x) for x in set(dice_roll)}

        # Iterate through the counts dictionary
        for num, count in counts.items():
            # Check for three or more of a kind
            if count >= 3:
                # Calculate score based on the number and count
                if num == 1:
                    score += 1000
                else:
                    score += num * 100
                # Handle additional scoring for four, five, or six of a kind
                if count == 4:
                    score += 1000 if num == 1 else num * 100
                elif count == 5:
                    score += 2000 if num == 1 else num * 200
                elif count == 6:
                    score += 3000 if num == 1 else num * 300
            # Check for individual 1s or 5s
            elif num == 1 or num == 5:
                score += (100 if num == 1 else 50) * count

        # Return the final calculated score
        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a specified number of dice.

        :param num_dice: Integer between 1 and 6 representing the number of dice to roll.
        :return: Tuple with random values between 1 and 6.
        """
        # Check if the number of dice is between 1 and 6, raise an error if not
        if not 1 <= num_dice <= 6:
            raise ValueError("Number of dice must be between 1 and 6")
        # Roll the specified number of dice and return a tuple of random values between 1 and 6
        return tuple(random.randint(1, 6) for _ in range(num_dice))

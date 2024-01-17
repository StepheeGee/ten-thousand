import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        if set(dice_roll) == set(range(1, 7)):
            return 1500
        if len(dice_roll) == 6 and all(dice_roll.count(value) == 2 for value in set(dice_roll)):
            return 1500
        score = 0
        counts = {x: dice_roll.count(x) for x in set(dice_roll)}
        for num, count in counts.items():
            if count >= 3:
                if num == 1:
                    score += 1000
                else:
                    score += num * 100
                if count == 4:
                    score += 1000 if num == 1 else num * 100
                elif count == 5:
                    score += 2000 if num == 1 else num * 200
                elif count == 6:
                    score += 3000 if num == 1 else num * 300
            elif num == 1 or num == 5:
                score += (100 if num == 1 else 50) * count
        return score
    @staticmethod
    def roll_dice(num_dice):
        if not 1 <= num_dice <= 6:
            raise ValueError("Number of dice must be between 1 and 6")
        return tuple(random.randint(1, 6) for _ in range(num_dice))
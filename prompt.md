# Prompt for Game Code Generation

1.16.24

## Prompt Source

ChatGPT 3.5

## Prompt Link

[ChatGPT 3.5](https://chat.openai.com/share/eee55385-63cc-4d31-9c3e-3d0a4b6c38f0)

[ChatGPT 3.5 - Round 2](https://chat.openai.com/share/5487eccd-790b-418a-9c61-4512f46ff977)

[ChatGPT 3.5 - Round 3](https://chat.openai.com/share/0b618276-ed7d-43ca-b922-e6059bafc61f)

[Partner's 4.0 Code](https://chat.openai.com/share/7197a5d8-9b61-4649-8181-8779d89d51f1)


## Prompt Text

User:
help me write code to pass these tests

help me create a Farkle game

## Prompt Code

### Best Output from ChatGPT 3.5 (fails 16 tests)

```python

import random

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]

    @staticmethod
    def calculate_score(dice):
        counts = [dice.count(i) for i in range(1, 7)]
        score = 0

        # Calculate score for ones
        score += counts[0] * 100

        # Calculate score for fives
        score += counts[4] * 50

        # Calculate score for three, four, five, and six of a kind
        for i in range(6):
            if counts[i] >= 3:
                if i == 0:  # If it's three ones
                    score += 1000
                else:
                    score += (i + 1) * 100 * (counts[i] // 3)

            # Check for four, five, and six of a kind
            if counts[i] >= 4:
                score += (i + 1) * 100 * (counts[i] // 4)

            if counts[i] == 5:
                score += (i + 1) * 100 * (counts[i] // 5)

            if counts[i] == 6:
                score += (i + 1) * 100 * (counts[i] // 6)

        # Calculate score for straight
        if all(counts[i] == 1 for i in range(6)):
            score += 1500

        # Calculate score for six ones
        score += (counts[0] // 6) * 2000

        return score
```

### Correct Code Output from ChatGPT 4.0

```python
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
```
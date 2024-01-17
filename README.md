# LAB - Class 06-08

## Project: The Ten Thousand Game (Farkle)

### Author: Stephanie G. Johnson

Partner: Chris Acosta

### Date: 

Class 06 - 1.16.24

Class 07 - 1.17.24

### Description:

10,000 is a classic dice game that combines luck and strategy. The game is played with six dice, and the objective is to score points by rolling specific combinations. The first player to reach 10,000 points wins.

1. **Objective:**
   - The goal is to be the first player to reach a predetermined point total, often 10,000 points.

2. **Setup:**
   - Players take turns rolling six dice.

3. **Scoring:**
   - Players score points based on specific combinations rolled:
     - Single 1: 100 points
     - Single 5: 50 points
     - Three of a kind (other than 1s and 5s): 100 times the face value (e.g., three 2s = 200 points)
     - Three 1s: 1,000 points
     - Four or more of a kind (other than 1s and 5s): Double the points for a three-of-a-kind for each additional die (e.g., four 3s = 300 points, five 3s = 600 points)
     - Straight (1-2-3-4-5-6): 1,500 points

4. **Rolling and Decision Making:**
   - After each roll, the player must set aside scoring dice and can choose to roll the remaining dice for additional points.
   - If a roll does not score any points, the player loses all points scored in that turn, and their turn ends.

5. **Ending a Turn:**
   - A player can choose to end their turn and bank the points earned, or they can continue rolling, risking a total loss of points in this round, to accumulate more points.

6. **Winning:**
   - The first player to reach the agreed-upon point total (e.g., 10,000 points) or surpass it in a final round wins the game.

### Links and Resources

[Game Rules](https://en.wikipedia.org/wiki/Dice_10000)

[Game Play](https://www.playonlinedicegames.com/farkle)

### Setup

#### Dependencies

- Python 3.6 or later
- Other libraries (install them using `pip install -r requirements.txt`, `pip install pytest, flo`, etc.)

#### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-tenthousand-project.git
   cd your-tenthousand-project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

#### Running the Application

To start the Ten Thousand game, run the following command:

   ```bash
   cd your-tenthousand-project
   python main.py
   ```

### Playing

python3 ten_thousand/play_game.py

#### Usage Instructions (if applicable)

   ```python
   from your_module import GameLogic

   # Example usage
   dice_roll = GameLogic.roll_dice(3)
   score = GameLogic.calculate_score(dice_roll)
   print(f"Rolled {dice_roll} and scored {score} points.")
   ```

#### Common Issues and Troubleshooting

If you encounter any issues during setup, check the following:

- Ensure Python 3.6 or later is installed.
- Verify that the required dependencies are installed.


#### Tests

To run the tests, run the following command:

```bash
cd your-tenthousand-project
pytest tests/
```

## Changelog

### Version 1.1.0 (Date: 1.17.24)

#### Added

- Implemented the ability for the player to set aside dice each roll.
- Added the feature to allow "banking" the current score or rolling again.
- Implemented tracking of the total score.
- Added tracking of the current round.

#### Updated

- Application should implement all features from this version.
- Application should allow the user to set aside dice each roll.
- Application should allow "banking" the current score or rolling again.
- Application should keep track of the total score.
- Application should keep track of the current round.

### Version 1.0.0 (Date: 1.16.24)

#### Added

- Initial release of the Ten Thousand game (Farkle).
- Implemented the core game rules, setup, scoring, rolling, decision-making, and winning conditions.
- Provided links to external game rules and gameplay references.
- Included setup instructions, dependencies, installation guide, and usage instructions.
- Added a section for playing the game and common issues and troubleshooting.
- Included a section for running tests.



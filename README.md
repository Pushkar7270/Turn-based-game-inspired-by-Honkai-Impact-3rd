## Turn-based-game-inspired-by-Honkai-Impact-3rd
A Python-based command-line RPG mini-game inspired by Honkai Impact 3rd. This project demonstrates Object-Oriented Programming (OOP) concepts in Python, featuring turn-based combat, RNG mechanics (Critical hits, Dodges, Parries), and a roster of distinct characters.

# 📖 About The Project
* This project simulates a boss battle where the player selects a "Valkyrie" to fight against the boss    Husk:Nihilus. The game utilizes a custom text-rendering engine to simulate a retro RPG feel and employs   probability-based combat mechanics.

# ✨ Features
* *3 Playable Characters*: Choose between Kiana, Mei, and Bronya, each with unique stats for HP, Attack, Speed, and Defense.

* *Dynamic Combat System*:
* Basic & Special Attacks: Choose your approach to dealing damage.
* RNG Mechanics: Every turn calculates probabilities for Critical Hits, Dodges, and Parries based on character stats.
* Boss AI: The boss (Husk:Nihilus) reacts to the player, dealing damage and utilizing the same combat mechanics (Crit/Dodge/Parry) against you.
* Immersive Text Effect: Custom "slow writing" script to create a typewriter effect for battle logs.

# 🎮 How to Play
* *Run the Game*: Execute the main.py script.
* *Select a Character*:
* *Kiana*: Balanced stats with high Critical chance.
* *Mei*: High Speed (Dodge) and balanced offense.
* *Bronya*: High Defense (Parry) and tanky HP.

# Battle Loop:
* On your turn, choose to perform a Basic Attack, Special Attack, or Forfeit.
* Watch the battle log to see if you land a Critical Hit, if the enemy Dodges, or if they Parry your attack.
* The Boss will retaliate on their turn.
* Win Condition: Reduce the Boss's HP to 0.
* Lose Condition: Your HP drops to 0 or you forfeited

# ⚔️ Combat Mechanics
* The game uses a probability list system (scale of 1-10) to determine combat outcomes:
* Critical Hit: Deals 2x Damage. Determined by the Crit stat.
* Parry: Reduces incoming damage by 50%. Determined by the DeF (Defense) stat.
* Dodge: Negates 100% of damage. Determined by the SPD (Speed) stat.
* Example: If a character has SPD 5, they have a 5/10 (50%) chance to dodge an incoming attack.

# 📂 File Structure
* *main.py*: The entry point of the game. Handles the game loop, character selection, and turn management.
* *Characters.py*: Defines the Characters class, player stats, and player attack logic.
* *Boss.py*: Defines the Boss class and the enemy AI logic.
* *slow_writing.py*: A utility module that handles the typewriter text effect for console output.

# 🛠️ Installation & Requirements
* Prerequisites
* Python 3.x

**Running the Game**
* Clone the repository or download the files.
* Navigate to the project directory.
* Run the main script:
* Bash
* python main.py
* *Note*: *No external libraries* (like pip packages) are required. The game uses standard Python libraries (random, time).

## Turn-based-game-inspired-by-Honkai-Impact-3rd
A Python-based command-line RPG mini-game inspired by Honkai Impact 3rd. This project demonstrates Object-Oriented Programming (OOP) concepts in Python, featuring turn-based combat, resource management (PP System), and RNG mechanics.

# 📖 About The Project
This project simulates a high-stakes boss battle where the player selects a "Valkyrie" to fight against the entity **"Sa"** (from Honkai Impact 3rd Part 1.5). The game utilizes a custom text-rendering engine to simulate a retro RPG feel and employs probability-based combat mechanics.

# ✨ Features
* **3 Playable Characters**: Choose between Kiana, Mei, and Bronya. Each character now has a **unique moveset** with different skills.
* **Boss (Sa)**: Fight against the tanky boss "Sa" (9000 HP), who possesses high Dodge/Parry rates and her own set of named special attacks.
* **PP (Power Point) System**: 
    * Special moves are no longer unlimited. 
    * You must manage **PP** (Turn limits) for your powerful skills. 
    * Once PP runs out, you are forced to use Basic Attacks.
* **Dynamic Combat**:
    * **Named Skills**: Use signature moves like *Shamash Unleashed* or *7 Thunders: Rumble*.
    * **RNG Mechanics**: Every turn calculates probabilities for Critical Hits, Dodges, and Parries based on stats.
    * **Boss AI**: The boss reacts to the player, selecting randomly from its own pool of 3 devastating moves.
* **Immersive Text Effect**: Custom "slow writing" script to create a typewriter effect for battle logs.

# 🎮 How to Play
1. **Run the Game**: Execute the `main.py` script.
2. **Select a Character**:
    * **Kiana**: High Critical Chance (50%). Moves: *Subspace Lance, Neko Charm, Shamash Unleashed*.
    * **Mei**: High Speed/Dodge (50%). Moves: *Searing Slash, 7 Thunders: Rumble, Fate Cutter*.
    * **Bronya**: High Defense/Parry (50%). Moves: *Cognitive Destruction, Selene, Quasi-black hole*.
3. **Battle Loop**:
    * On your turn, select an action from the menu:
        * `1` **Basic Attack**: Standard damage, unlimited use.
        * `2-4` **Special Skills**: High damage, but consumes **PP**.
        * `5` **Forfeit**: Surrender the battle immediately.
    * Watch the battle log for Critical Hits, Dodges, or Parries.
    * The Boss will retaliate with moves like *Matter Erasure* or *Power of Samsara*.

# ⚔️ Combat Mechanics
* **PP Management**:
    * **Move 1 & 2**: 10 Uses (PP) each.
    * **Move 3 (Ultimate)**: 5 Uses (PP) only. Use them wisely!
* **Probability System**:
    * **Critical Hit**: Deals 2x Damage. (Based on Crit stat).
    * **Parry**: Reduces incoming damage by 50%. (Based on DEF stat).
    * **Dodge**: Negates 100% of damage. (Based on SPD stat).
* **Win/Lose Condition**: Reduce "Sa's" HP to 0 to win. You lose if your HP hits 0 or you forfeit.

# 📂 File Structure
* **main.py**: The entry point. Handles the game loop, stats initialization, and turn logic.
* **Characters.py**: Defines the `Characters` class, including the new PP tracking and input validation logic.
* **Boss.py**: Defines the `Boss` class with specific AI logic and enemy movesets.
* **slow_writing.py**: Utility module for the typewriter text effect.

# 🛠️ Installation & Requirements
* **Prerequisites**: Python 3.x
* **Running the Game**:
    1. Clone the repository or download the files.
    2. Navigate to the project directory.
    3. Run the command: `python main.py`
    *Note: No external libraries (like pip packages) are required. The game uses standard Python libraries (random, time).*
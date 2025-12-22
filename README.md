## ⚔️ Honkai RPG: Data-Driven Turn-Based Engine
- A professional refactoring of a Python-based CLI RPG inspired by Honkai Impact 3rd. This project demonstrates a transition from a hardcoded script to a scalable, Data-Driven Architecture using Object-Oriented Programming (OOP) and JSON serialization.

## 🚀 The Refactoring Journey (Legacy vs. Modern)
- This repository contains two versions of the game to showcase architectural growth:
- *Legacy Version (/old_code)*: A beginner-friendly, hardcoded script where character stats and logic are intertwined.
- *Refactored Version (Root)*: An intermediate-level engine that decouples game logic from character data using JSON "databases".

## ✨ Key Technical Features
- *OOP & Dataclasses*: Utilizes Python @dataclass for clean, robust entity management (HP, Speed, Defense, Crit).
- *JSON Serialization*: All Valkyrie and Boss stats are externalized in Characters.json. The engine "rehydrates" this data into Python objects at runtime.
- *Scalable Move System*: A custom Move class handles damage and PP (Power Points) management independently for every entity.
- *Internal State Logic*: Uses __post_init__ to automatically calculate max_hp and max_pp during object creation.
- *Dynamic Battle Engine*: A centralized Battle_logic controller that handles turn-order, RNG calculations (Crit/Dodge/Parry), and win/loss conditions.

## 📂 Project Architecture
- *New_main.py*: The game controller. Manages user selection and initiates the battle sequence.
- *Entites.py*: The Data Models. Contains the Entity and Move classes that define game characters.
- *File_handler.py*: The Data Access Layer. Safely handles JSON loading and saving to prevent data corruption.
- *available_characters.py*: A developer tool used to generate and update the Characters.json "database".
- *Game_work_flow.py*: Contains the core combat algorithm and turn-based logic.

## 🎮 How it Works (Under the Hood)
- *Data Loading*: The engine calls get_game_entities() to parse Characters.json.
- *Object Rehydration*: Dictionary data is converted into Entity and Move objects.
- *Deployment*: The user selects a Valkyrie, and the engine injects those specific stats into the Battle_logic.
- *Simulation*: Combat is simulated using probability-based RNG (Crit/Dodge) until an HP value reaches zero.

## 🛠️ Installation & Setup
- *Prerequisites*: Python 3.11+ (uses modern dataclass features).
- *Clone*: git clone [(https://github.com/Pushkar7270/Turn-based-game-inspired-by-Honkai-Impact-3rd)]
- *Initialize Data*: Run python available_characters.py to generate the initial character database.
- *Launch*: Run python New_main.py to start the game.
# ⚔️ Honkai RPG: Data-Driven Turn-Based Engine
- A professional refactoring of a Python-based CLI RPG inspired by Honkai Impact 3rd. This project demonstrates a transition from a hardcoded script to a scalable, Data-Driven Architecture using Object-Oriented Programming (OOP) and JSON serialization.

# 🚀 The Refactoring Journey (Legacy vs. Modern)
- This repository contains two versions of the game to showcase architectural growth:
- Legacy Version (/old_code): A beginner-friendly, hardcoded script where character stats and logic are intertwined.This code can be used to understand the core mechanics of the game.
- Refactored Version (Root): An intermediate-level engine that decouples game logic from character data using JSON "databases" and features a modern graphical user interface.
- you can add lots of characters without touching the core engine.

# ✨ Key Technical Features
 * OOP & Dataclasses* : Utilizes Python @dataclass for clean, robust entity management (HP, Speed, Defense, Crit).
 * Modern GUI *: Built with customtkinter, featuring a Main Menu, Character Selection windows, and a dedicated Battle interface.
 * Automated Simulations *: A simulation engine capable of running hundreds of automated battles to gather balancing data.
 Additionally your own gameplay can be used as data to compare real and computer play throughs for smooth balancing of characters.
 * Data Visualization *: Integrated matplotlib dashboards that analyze win rates, move usage, and average damage for every Valkyrie and Boss.
 * Internal State Logic *: Uses __post_init__ to automatically calculate max_hp and max_pp during object creation.

# 📂 Project Architecture
* New_main.py *: The central game controller. Manages the main menu and orchestrates the transition between selection and battle.
* Entites.py *: The Data Models. Contains the Entity and Move classes that define game characters.
* data_analysis_gui.py *: The analytics dashboard. Visualizes battle data from both simulations and real player games.
* simulations.py *: The stress-testing tool. Runs batch simulations to populate simulation_data.json.
* Game_work_flow.py *: Contains the core combat algorithm and turn-based logic.
* UI/ *: Directory containing modular GUI components like Battle_window.py and selection_window.py.

# 🎮 How it Works 
* Data Loading: The engine calls get_game_entities() to parse Characters.json.
* Object Rehydration : Dictionary data is converted into Entity and Move objects at runtime.
* Simulation & Logging " Battles are logged into JSON files, tracking every turn, actor, and damage value for post-game analysis.
* Analytics : The DataAnalysisWindow filters these logs to generate performance charts comparing "Real Game" play vs. "Simulation" RNG.

# 🛠️ Installation & Setup
* * Prerequisites : Python 3.11+ (uses modern dataclass features and customtkinter).
* * Clone : git clone [https://github.com/Pushkar7270/Turn-based-game-inspired-by-Honkai-Impact-3rd]
* * Dependencies :  pip install customtkinter matplotlib numpy pillow
* * Initialize Data : Run python available_characters.py to generate the initial character database.

Launch: Run python New_main.py to start the game and access the analysis dashboard

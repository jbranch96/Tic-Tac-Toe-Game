# Tic-Tac-Toe GUI App

This folder contains source code for a Python based GUI implementation of the game Tic-Tac-Toe

 ## Table of Contents
 
 - [Game Modes](#game-modes)
 - [Python GUI](#python-gui)
 - [Steps to Run the Code](#steps-to-run-the-code)
 - [Project Code Structure](#project-code-structure)
 - [Tech Used](#tech-used)

# Game Modes
## 2-Player Mode
In this mode, two players take turns making their moves on the game board. Player X always initially goes first, followed by Player O. The game continues until one player achieves three in a row (horizontally, vertically, or diagonally) or until all positions on the board are filled, resulting in a draw. After each game, the player whose turn it would have been goes first in the next round.

## Vs Computer Mode
In the Vs Computer mode, one user competes against the computer. The computer's difficulty can be adjusted to enhance gameplay. The available difficulty settings are:

***Easy***: The computer makes random moves, providing a very casual experience.

***Medium***: The computer attempts to block the player’s winning moves but may overlook some opportunities to win for itself. This level offers a moderate challenge.

***Hard***: The computer employs heuristic logic to make strategic decisions. It actively blocks the player's winning moves while seeking to create its own winning opportunities, making it more competitive.

***Impossible***: The computer utilizes the minimax algorithm, effectively making it "impossible" for the user to win.
				
# Python GUI:
![Py-Tac-Toe-Tk-GUI](Py-Tac-Toe-Tk-GUI.PNG)

## Steps to Run the Code
        
- 1. Clone the Repository: "git clone https://github.com/jbranch96/Tic-Tac-Toe-Game.git"
- 2. Run:
     - Navigate to the Python folder and run main.py: **Python main.py**

# Project Code Structure

        │
        ├── Python/  
            ├── main.py                     # Main entry point for the Py-Tac-Toe application
            ├── gui_main.py                 # Main GUI class that invokes the other classes defined in the other project files
            ├── gui_layout.py               # Handles configuring the GUI layout 
            ├── gui_controller.py           # Handles top-level game logic that requires interaction with the GUI
            ├── game_logic.py               # Handles lower-level internal game logic and game state management
            └── Py-Tac-Toe_icon.png         # Icon used in as the application logo

## Tech Used
- Python 3.11.5 and Tkinter

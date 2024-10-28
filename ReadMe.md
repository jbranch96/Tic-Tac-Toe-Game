This folder contains source code and an executable build for 2 implmentations of Tic-Tac-Toe

One application is written in LabVIEW, while the other application is written in Python (Tkinter GUI application)

LabVIEW source code written in LabVIEW 2021 - 32 bit, Windows 10 enviroment

The LabVIEW 2021 Run-Time engine download executable included within the LabVIEW folder may need to be run first in order to run the LabVIEW-built application.

##LabVIEW GUI:
![Tic-Tac-Toe-LV-GUI](Tic-Tac-Toe-LV-GUI.PNG)

## LabVIEW Project Structure

        │
        ├── Builds/                         # Compiled LabVIEW executable (*requires Run-Time Engine installed on machine running the executable)
        ├── Code/                           # Source files
        │   └── Controls/    				# Custom controls for application
		│	└── Sub VIs/					# Sub-VIs for application
		│	└── Main.vi						# Main application VI
		│	└── Tic-Tac-Toe Game.aliases
		│	└── Tic-Tac-Toe Game.lvlps 
		│	└── Tic-Tac-Toe Game.lvproj    # LabVIEW project file
        └── Run-Time Engine                # Offline Run-Time Engine installer for LabVIEW 2021 (x86_21.0)
		
		
##Python GUI:
![Py-Tac-Toe-Tk-GUI](Py-Tac-Toe-Tk-GUI.PNG)

## Python Project Structure

        │
        ├── main.py                        # Main entry point for the Py-Tac-Toe application
        ├── gui_main.py                    # Main GUI class that invokes the other classes defined in the other project files
        ├── gui_layout.py                  # Handles configuring the GUI layout 
        ├── gui_controller.py              # Handles top-level game logic that requires interaction with the GUI
		├── game_logic.py                  # Handles lower-level internal game logic and game state management
        └── Py-Tac-Toe_icon.png            # Icon used in as the application logo
		
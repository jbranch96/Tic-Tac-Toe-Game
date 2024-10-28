"""
This .py file is the main entry point for the PyTacToe application.
This calls the constructor for the PyTacToeGUI class, which handles creating the GUI and invoking the other classes in the project.

It terms of gameplay behavior, the project as implemented, will always have the user go first before the computer does in 'vs-computer' mode.
In '2-Player' mode, the person who lost the previous game will start the next game.  As a default, upon initiatilization, the 'X' user starts.
"""

import tkinter as tk # import tkinter module for creating GUI
from gui_main import PyTacToeGUI

def main() -> None:
    root = tk.Tk() # create self.root window
    PyTacToeGUI(root, width=660, height=340)
    root.mainloop() # execute tkinter 


if __name__ == "__main__":
    main()
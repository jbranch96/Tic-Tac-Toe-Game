"""
This .py file defines the GUI class to create the PyTacToeGUI.
It also calls constructors for the following classes: PyTacToeGame, PyTacToeLayout, PyTacToeGameController, PyTacToeStateUpdater

The PyTacToeGame class contains the internal game/state logic. 

The PyTacToeLayout class handles defining the GUI layout.

The PyTacToeGameController class handles game logic that requires interaction w/the GUI, often calling methods from the PyTacToeGame class.
This class serves as an intermediary between the internal game/state logic and the GUI.

The PyTacToePlayerStateUpdater class contains methods for setting/updating the GUI components.

It is not intended to invoke this alone, but rather to create an instantiation of this class within the main app .py file.
"""

import tkinter as tk # import tkinter module for creating GUI
from tkinter import ttk, messagebox
from game_logic import PyTacToeGame
from gui_layout import PyTacToeLayout
from gui_controller import PyTacToeGameController, PyTacToePlayerStateUpdater

class PyTacToeGUI(tk.Frame):
        
    def __init__(self, root : tk.Tk, width : int, height : int):
        super().__init__(root)
        self.root : tk.Tk = root
        self.width : int = width
        self.height : int = height
        self.game = PyTacToeGame()
        self.layout = PyTacToeLayout(root=self.root, width=self.width, height=self.height)
        self.state_updater = PyTacToePlayerStateUpdater(game=self.game, layout=self.layout, root=self.root)
        self.game_controller = PyTacToeGameController(game = self.game, layout=self.layout, state_updater=self.state_updater, root=self.root)
        self.mode_var = tk.StringVar(value='2-Player')  # Default mode : 2-Player
        self.player1_var = tk.StringVar(value='Player 1')  # Default name for player 1
        self.player2_var = tk.StringVar(value='Player 2')  # Default name for player 2
    
        self.layout.setup_main_window()
        self.layout.setup_frames(modal_func=self.open_game_mode_modal, button_func=self.handle_button_click, empty_mark=self.game.empty_mark)
        self.initialize_components()
    

    def initialize_components(self) -> None:
        """This function initializes the GUI components for date/time and launches the modal to ask the user which game mode to start with (2-Player or vs-computer)."""
        self.state_updater.set_entry_current_date()
        self.state_updater.set_entry_current_time()
        self.open_game_mode_modal()
        

    def open_game_mode_modal(self):
        """This function creates a modal window that is used to capture game mode (2-player or vs-computer)."""
        modal_window = tk.Toplevel(self.root)
        modal_window.title("Select Game Mode")
        modal_window.geometry("300x150")
        self.layout.center_window(window=modal_window, width=300, height=150)

        ttk.Label(modal_window, text="Choose Game Mode:").pack(pady=10)

        # Radio buttons for game mode selection
        ttk.Radiobutton(modal_window, text="2-Player", variable=self.mode_var, value="2-Player").pack(anchor='w')
        ttk.Radiobutton(modal_window, text="Vs Computer", variable=self.mode_var, value="vs-computer").pack(anchor='w')

        # Button to confirm selection
        confirm_button = ttk.Button(modal_window, text="Confirm", command=lambda: self.confirm_game_mode_selection(modal_window))
        confirm_button.pack(pady=10)

        modal_window.grab_set()  # Make this window modal
        self.root.wait_window(modal_window)  # Wait for the modal to close
        self.game_controller.reset_game() # After each call, reset the game state


    def confirm_game_mode_selection(self, modal_window):
        selected_mode: str = self.mode_var.get()
        messagebox.showinfo("Game Mode Selected", f"You selected: {selected_mode}")
        modal_window.destroy()  # Close the modal window
        
        if selected_mode == "vs-computer":
            self.player1_var.set(value="User")
            self.player2_var.set(value="Computer")

        if selected_mode == "2-Player":
            self.player1_var.set(value="Player-1") # Set the player1_var to 'Player-1' as a default
            self.player2_var.set(value="Player-2") # Set the player2_var to 'Player-2' as a default
            self.open_get_player_names_modal()
                  
        self.state_updater.update_entry_player1(player1_name=self.player1_var.get())
        self.state_updater.update_entry_player2(player2_name=self.player2_var.get())
        self.game_controller.send_mode_update_to_controller_class(mode=selected_mode)


    def open_get_player_names_modal(self) -> None:
        """This functions creates a modal window that is used to get player names."""
        modal_window = tk.Toplevel(self.root)
        modal_window.title("Enter Player Names")
        modal_window.geometry("300x150")
        self.layout.center_window(window=modal_window, width=300, height=150)

        ttk.Label(modal_window, text="Enter Player Names:").pack(pady=10)
        ttk.Entry(modal_window, text='Player1 Name', textvariable=self.player1_var).pack(anchor='w')
        ttk.Entry(modal_window, text='Player2 Name', textvariable=self.player2_var).pack(anchor='w')

        # Button to confirm selection
        confirm_button = ttk.Button(modal_window, text="Confirm", command=modal_window.destroy)
        confirm_button.pack(pady=10)

        modal_window.grab_set()  # Make this window modal
        self.root.wait_window(modal_window)  # Wait for the modal to close    


    def handle_button_click(self, position : int) -> None:
        """This function is used to handle button presses on the tic-tac-toe grid."""
        if self.game.make_move(position):
            self.game.switch_player()
            self.game_controller.update_gui_board()
            p1_var = self.player1_var.get()
            p2_var = self.player2_var.get()
            
            if self.game_controller.check_winner_and_reset(player1_var=p1_var, player2_var=p2_var) or self.game_controller.check_tie_and_reset():
                return  # Exit early if the game has ended

            # Only make a computer move if the mode is set to 'vs-computer'
            if self.mode_var.get() == "vs-computer":
                self.game.computer_move()
                self.game_controller.update_gui_board()
                self.game_controller.check_winner_and_reset(player1_var=self.player1_var.get(), player2_var=self.player2_var.get())
            
            self.state_updater.update_current_player_display()
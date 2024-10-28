"""
This .py file defines the PyTacToeGameController and PyTacToePlayerStateUpdater classes.

The PyTacToeGameController class handles game logic that requires interaction w/the GUI, often calling methods from the PyTacToeGame class.
This class serves as an intermediary between the internal game/state logic and the GUI.

The PyTacToePlayerStateUpdater class contains methods for setting/updating the GUI components.

It is not intended to invoke these classes alone, but rather to create instantiations of these class within the main GUI .py file.
"""

import tkinter as tk # import tkinter module for calling tkinter methods
from datetime import datetime
from game_logic import PyTacToeGame
from gui_layout import PyTacToeLayout

X_COLOR_STR_CONST = "dark red"
O_COLOR_STR_CONST = "black"

class PyTacToePlayerStateUpdater:

    def __init__(self, game : PyTacToeGame, layout : PyTacToeLayout, root : tk.Tk):
        self.game : PyTacToeGame = game
        self.layout : PyTacToeLayout = layout
        self.root : tk.Tk = root


    def set_entry_current_date(self) -> None:
        """This function sets the current date on the GUI, should only be called once on GUI initialization."""
        self.layout.entryfield_current_date.config(state="normal")
        self.layout.entryfield_current_date.insert(index=-1, string=datetime.now().strftime("%a, %b %d, %Y"))
        self.layout.entryfield_current_date.config(state="readonly")


    def set_entry_current_time(self) -> None:
        """This functions sets the current time on the GUI, this functions sets up a task to repeat every 1 second(s)."""
        self.layout.entryfield_current_time.config(state="normal")
        self.layout.entryfield_current_time.delete(first=0, last=tk.END)
        self.layout.entryfield_current_time.insert(index=-1, string=datetime.now().strftime("%I:%M:%S %p"))
        self.layout.entryfield_current_time.config(state="readonly")
        self.root.after(1000, self.set_entry_current_time)


    def update_current_player_display(self) -> None:
        """This functions updates the current player entry field on the GUI."""
        self.layout.entryfield_current_player_turn.config(state="normal")
        self.layout.entryfield_current_player_turn.delete(first=0, last=tk.END)
        
        if self.game.current_player == 'X': self.layout.entryfield_current_player_turn.config(fg=X_COLOR_STR_CONST)
        else: self.layout.entryfield_current_player_turn.config(fg=O_COLOR_STR_CONST)
        
        self.layout.entryfield_current_player_turn.insert(index=-1, string=f"Current Player: {self.game.current_player}")
        self.layout.entryfield_current_player_turn.config(state="readonly") 


    def update_entry_player1(self, player1_name : str) -> None:
        """This functions updates the player1 entry field on the GUI."""
        self.layout.entryfield_player1.config(state="normal", fg = X_COLOR_STR_CONST)
        self.layout.entryfield_player1.delete(first=0, last=tk.END)
        self.layout.entryfield_player1.insert(index=-1, string=f"X  | {player1_name}")
        self.layout.entryfield_player1.config(state="readonly")


    def update_entry_player2(self, player2_name : str) -> None:
        """This functions updates the player2 entry field on the GUI."""
        self.layout.entryfield_player2.config(state="normal")
        self.layout.entryfield_player2.delete(first=0, last=tk.END)
        self.layout.entryfield_player2.insert(index=-1, string=f"O | {player2_name}")
        self.layout.entryfield_player2.config(state="readonly")

    
    def update_game_win_record(self, record : str) -> None:
        """This functions updates the game win record textfield on the GUI after each game."""
        self.layout.textfield_game_record.insert(index=tk.END, chars=record+"\n")
        self.layout.textfield_game_record.see(tk.END)


class PyTacToeGameController:
    
    def __init__(self, game : PyTacToeGame, layout : PyTacToeLayout, state_updater : PyTacToePlayerStateUpdater, root : tk.Tk):
        self.game : PyTacToeGame = game
        self.layout : PyTacToeLayout = layout
        self.state_updater : PyTacToePlayerStateUpdater = state_updater
        self.mode : str = '2-Player' # Default mode : 2-Player, updated when user selects a different mode (passed down from top-level GUI class)
        self.root : tk.Tk = root
    

    def check_winner_and_reset(self, player1_var : str, player2_var : str) -> bool:
        """This functions checks if there is a winner, if there is it returns True, otherwise it returns false.
        It also prints out a message to the user(s), indicating that the game is over. 
        """
        winner_char = self.game.check_winner()
       
        if not winner_char: return False
       
        if winner_char == "X": winner = player1_var
        else: winner = player2_var

        x, y = self.root.winfo_x(), self.root.winfo_y()  
        self.root.geometry(f"+{x + 50}+{y}") # Moves the main window slightly to the right

        message = f"{winner} wins!"
        tk.messagebox.showinfo("Game over", message)

        self.root.geometry(f"+{x}+{y}")  # Moves the main window back to its original position
       
        self.state_updater.update_game_win_record(record=message)
        self.reset_game()
       
        return True
        

    def check_tie_and_reset(self) -> bool:
        """This functions checks if the game state is in a tie(draw), if it is it returns True, otherwise it returns false.
        It also prints out a message to the user(s), indicating that the game is over. 
        """
        draw = self.game.check_tie()
        
        if not draw: return False

        x, y = self.root.winfo_x(), self.root.winfo_y()  
        self.root.geometry(f"+{x + 50}+{y}") # Moves the main window slightly to the right
        
        message = "It's a draw!"
        tk.messagebox.showinfo("Game over", message)

        self.root.geometry(f"+{x}+{y}")  # Moves the main window back to its original position
        
        self.state_updater.update_game_win_record(record=message)
        self.reset_game()
        
        return True


    def reset_game(self) -> None:
        """This function is used to reset the game state and to reset the GUI."""
        self.game.reset_game()
        
        if self.mode == "vs-computer": self.game.current_player = 'X'
        
        self.update_gui_board()
        self.state_updater.update_current_player_display()  # Reset the current player display

    
    def send_mode_update_to_controller_class(self, mode : str) -> None:
        """This function is used to retrieve the selected game mode upon any user changes to game mode selection.
        Valid game mode are: '2-Player' or 'vs-computer'
        """
        self.mode = mode


    def update_gui_board(self) -> None:
        """This functions updates the tic-tac-toe board on the GUI, and is called after game state changes."""
        for i, button in enumerate(self.layout.buttons):
            button.config(text=self.game.board[i])
            
            if self.game.board[i] == 'X': button.config(fg=X_COLOR_STR_CONST)
            if self.game.board[i] == 'O': button.config(fg=O_COLOR_STR_CONST)  
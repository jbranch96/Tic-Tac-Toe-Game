"""
This .py file defines the PyTacToeGame class which is used to contain the inner game logic/state.  
It is not intended to invoke this alone, but rather to create an instantiation of this class within the main GUI .py file.
"""

import random

class PyTacToeGame:

    def __init__(self):
        self.empty_mark : str = ' ' # Obvious constraint for this is that it cannot be 'X' or 'O', but could be any other str really, ' ' is simple and makes sense
        self.board : list[str] = [self.empty_mark for _ in range(9)] # Game board modeled as 1-D list of str ('X', 'O', or self.empty_mark are the only valid entries) 
        self.current_player : str = 'X'


    def check_winner(self) -> None | str:
        """This functions contains the inner game state logic to check if their is a winner based on the current game state."""
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
                                (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
                                (0, 4, 8), (2, 4, 6)]            # two diagonals
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != self.empty_mark:
                return self.board[combo[0]]
        return None
    

    def check_tie(self) -> None | str:
        """This functions contains the inner game state logic to check if the game is in a tie(draw) based on the current game state."""
        if self.empty_mark in self.board: return None
        else: return self.empty_mark
        
    
    def computer_move(self) -> None:
        """This functions contains the logic for performing the move for the computer opponent.
        Used if 'vs-computer' mode is the currently selected game mode. 
        It handles updating the board state within this class and switching to the user once the move is complete.
        Future plans in place to refactor this function to handle different logic implementations for computing the next computer move.
        """
        empty_positions = [i for i in range(9) if self.board[i] == self.empty_mark]
        if empty_positions:
            move = random.choice(empty_positions) # comp move is random, would like to refactor this to be able to use different implementations for move calculations
            self.board[move] = self.current_player
            self.switch_player()


    def make_move(self, position : int) -> bool:
        """This function checks if the requested user move is valid, if the move requested is invalid it does not perform any move and returns False.
        Otherwise, it performs the move, updating the board state within the class and returns True.
        """
        if self.board[position] != self.empty_mark: return False
        self.board[position] = self.current_player
        return True
    

    def reset_game(self) -> None:
        """This function resets the board state within the class back to default (all cells marked with self.empty_mark)."""
        self.board = [self.empty_mark for _ in range(9)]


    def switch_player(self) -> None:
        """This functions switches the current player in the game state."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
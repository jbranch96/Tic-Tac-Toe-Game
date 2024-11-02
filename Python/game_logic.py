"""
This .py file defines the PyTacToeGame class which is used to contain the inner game logic/state.  
It is not intended to invoke this alone, but rather to create an instantiation of this class within the main GUI .py file.
"""

from enum import Enum
import random

class PyTacToeGameComputerLogic(Enum):
    RANDOM = 0
    HEURISTIC = 1
    HEURISTIC_DIFFICULT = 2


class PyTacToeGame:

    def __init__(self):
        self.empty_mark : str = ' ' # Obvious constraint for this is that it cannot be 'X' or 'O', but could be any other str really, ' ' is simple and makes sense
        self.board : list[str] = [self.empty_mark for _ in range(9)] # Game board modeled as 1-D list of str ('X', 'O', or self.empty_mark are the only valid entries) 
        self.computer_logic_enum_enum = PyTacToeGameComputerLogic.HEURISTIC
        self.current_player : str = 'X'
        self.winning_combinations : list[tuple[int]] = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
            (0, 4, 8), (2, 4, 6)             # two diagonals
                        ]            


    def check_winner(self) -> None | str:
        """This functions contains the inner game state logic to check if there is a winner based on the current game state."""
        for combo in self.winning_combinations:
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
        """
        empty_positions = [i for i in range(9) if self.board[i] == self.empty_mark]

        if empty_positions:
            if self.computer_logic_enum == PyTacToeGameComputerLogic.RANDOM:
                move = random.choice(empty_positions) 
            elif self.computer_logic_enum in {PyTacToeGameComputerLogic.HEURISTIC, PyTacToeGameComputerLogic.HEURISTIC_DIFFICULT}:
                move = self.computer_move_heuristic_logic(empty_positions=empty_positions)
            else:
                raise ValueError("Invalid selection for computer logic enumeration.")

            self.board[move] = self.current_player
            self.switch_player()


    def computer_move_heuristic_logic(self, empty_positions : list[int]) -> int:
        """
        Uses heuristic logic to compute the next move for the computer opponent to take in the game.
                    0 | 1 | 2
        Board -->   3 | 4 | 5
                    6 | 7 | 8
        """
        
        # 1 - Check for winning move for computer, if there is take it
        temp_result : int = self.scan_board_for_winning_move(board_mark=self.current_player, empty_positions=empty_positions) 
        if temp_result != -1: return temp_result # func returns -1 if there isn't a winning move

        # 2 - Check for winning move for user, if there is block it
        if self.computer_logic_enum == PyTacToeGameComputerLogic.HEURISTIC_DIFFICULT:
            temp_user_char: str = 'O' if self.current_player == 'X' else 'X'
            temp_result = self.scan_board_for_winning_move(board_mark=temp_user_char, empty_positions=empty_positions)
            if temp_result != -1: return temp_result # func returns -1 if there isn't a winning move
        
        # 3 - Take Center if availible (4)
        if 4 in empty_positions: return 4

        # 4 - Take Corner opposite from a user mark (u:0,8 -> c:8,0) or (u:2,6 -> c:6,2)
        if 0 not in empty_positions and 8 in empty_positions: return 8
        if 8 not in empty_positions and 0 in empty_positions: return 0
        if 2 not in empty_positions and 6 in empty_positions: return 6
        if 6 not in empty_positions and 2 in empty_positions: return 2

        # 5 - Take any empty Corner (0, 2, 6, 8)
        if 0 in empty_positions: return 0
        if 2 in empty_positions: return 2
        if 6 in empty_positions: return 6
        if 8 in empty_positions: return 8

        # 6 - Take any empty Side (1, 3, 5, 7)
        if 1 in empty_positions: return 1
        if 3 in empty_positions: return 3
        if 5 in empty_positions: return 5
        if 7 in empty_positions: return 7


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

    
    def scan_board_for_winning_move(self, board_mark : str, empty_positions : list[int]) -> int:
        """This is a helper function that can be used to scan the current game state to evaluate if there is a winning move that could be made."""
        for pos in empty_positions:
            temp_board : list[int] = self.board.copy() # Make shallow copy, separate obj refs in this case as desired
            temp_board[pos] = board_mark
            for combo in self.winning_combinations:
                if temp_board[combo[0]] == temp_board[combo[1]] == temp_board[combo[2]] != self.empty_mark:
                    for i in range(3):
                        if self.board[combo[i]] == self.empty_mark: 
                            return combo[i]

        return -1
    

    def send_difficulty_selected_to_game_class(self, difficulty : int) -> None:
        """This function is used to retrieve the selected game difficulty.
        Valid difficulty selections are: 'EASY:0' 'MEDIUM:1' or 'HARD:2'
        """
        self.computer_logic_enum = PyTacToeGameComputerLogic(difficulty)


    def switch_player(self) -> None:
        """This functions switches the current player in the game state."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
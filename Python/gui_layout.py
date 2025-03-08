"""
This .py file defines the GUI layout class to create the frames and layouts for the PyTacToeGUI.
It is not intended to invoke this alone, but rather to create an instantiation of this class within the main GUI .py file.
"""

import tkinter as tk  # import tkinter module for creating GUI layout/frames components
from tkinter import ttk, PhotoImage
from typing import Callable

class PyTacToeLayout:

    def __init__(self, root: tk.Tk, width: int, height: int):
        self.bg_color1: str = "#303030"
        self.bg_color2: str = "#505050"
        self.root: tk.Tk = root
        self.width: int = width
        self.height: int = height
        self.x_offset = 0
        self.y_offset = 0

        try: 
            self.icon = PhotoImage(file="Py-Tac-Toe_small.png",height=15, width=30)
        except tk.TclError:  #If image isn't found for the app icon, then just continue on. Where icon is used need to handle except case.
            pass

        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.info_frame = tk.Frame(self.main_frame)
        self.grid_frame = tk.Frame(self.main_frame)
        

    def center_window(self, window, width: int, height: int) -> None:
        """Helper function that centers a window/frame on the screen, works for modals as well."""
        window.update_idletasks()  # Ensures window size is current
        screen_width: int = window.winfo_screenwidth()
        screen_height: int = window.winfo_screenheight()
        x: int = (screen_width - width) // 2
        y: int = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")


    def create_custom_title_bar(self) -> None:
        """Creates a custom title bar for the window with a title label, image, and a close button."""
        # Create a custom title bar frame
        self.title_bar = tk.Frame(self.root, bg=self.bg_color2, height=40)
        self.title_bar.grid(row=0, column=0, sticky="ew")  # Using grid here

        # Title label in the custom title bar
        title_label = tk.Label(self.title_bar, text="Py-Tac-Toe", fg="white", bg=self.bg_color1, font=("Arial", 14))
        title_label.grid(padx=10, pady=5, row=0, column=1, sticky="w")

        if self.icon:
            # Display image on the left side of the title bar
            image_label = tk.Label(self.title_bar, image=self.icon, bg=self.bg_color2)
            image_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Add a close button to the title bar
        close_button = tk.Button(self.title_bar, text="X", fg="red", bg=self.bg_color1, width=2, command=self.root.quit)
        close_button.grid(padx=(self.width-200), pady=5, row=0, column=2, sticky="e")

        # Bind mouse events for dragging the title bar
        self.title_bar.bind("<Button-1>", self.start_drag)
        self.title_bar.bind("<B1-Motion>", self.drag_window)
        self.title_bar.bind("<ButtonRelease-1>", self.stop_drag)

        self.center_window(window=self.root, width=self.width, height=self.height)


    def start_drag(self, event: tk.Event) -> None:
        """Start dragging the window."""
        self.x_offset = event.x
        self.y_offset = event.y


    def drag_window(self, event: tk.Event) -> None:
        """Drag the window while the mouse is moving."""
        delta_x = event.x - self.x_offset
        delta_y = event.y - self.y_offset
        new_x = self.root.winfo_x() + delta_x
        new_y = self.root.winfo_y() + delta_y
        self.root.geometry(f"+{new_x}+{new_y}")


    def stop_drag(self, event: tk.Event) -> None:
        """Stop dragging the window."""
        pass


    def setup_main_window(self) -> None:
        """This function sets up the main TK window for the application."""
        if hasattr(self, "icon"): 
            self.root.iconphoto(True, self.icon)  # Important to check for attr existence, since if image not found icon attr not created
        self.root.title("Py-Tac-Toe")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root["bg"] = self.bg_color1
        self.root.overrideredirect(True)  # Remove the default title bar
        self.create_custom_title_bar()  # Call the function to create the custom title bar


    def setup_frames(self, modal_func: Callable[[], None], button_func: Callable[[int], None], empty_mark: str) -> None:
        """This function sets up the grid of the TK frames and calls the method that populates the GUI components on the frames."""
        self.main_frame["bg"] = self.bg_color1
        self.info_frame["bg"] = self.bg_color1
        self.grid_frame["bg"] = self.bg_color1
        self.main_frame.grid(row=1, column=0, sticky="NSEW")  # Use grid for main frame
        
        # Set grid for internal frames
        self.info_frame.grid(row=0, column=0, sticky="NSEW")
        self.grid_frame.grid(row=0, column=1, sticky="NSEW", padx=(20, 0), pady=(20, 0))    
        self.populate_components_info_frame(modal_func=modal_func)  # instantiate the info frame (local method)
        self.create_tic_tac_toe_board(button_func=button_func, empty_mark=empty_mark)


    def populate_components_info_frame(self, modal_func: Callable[[], None]) -> None:
        """This function populates the GUI components on info_frame."""
        # Button to open the game mode selection modal
        select_mode_button = tk.Button(self.info_frame, text="Choose Game Mode", fg="darkred", bg=self.bg_color2, command=modal_func)
        select_mode_button.grid(row=0, column=0, sticky='w', pady=5)
        
        # Player 1
        self.label_player1 = tk.Label(self.info_frame, text="Player 1", bg=self.bg_color1)
        self.label_player1.grid(row=1, column=0, sticky='w', pady=5)
        self.entryfield_player1 = tk.Entry(self.info_frame, width=25, state="readonly")
        self.entryfield_player1.grid(row=1, column=1, pady=5)

        # Player 2
        self.label_player2 = tk.Label(self.info_frame, text="Player 2", bg=self.bg_color1)
        self.label_player2.grid(row=2, column=0, sticky='w', pady=5)
        self.entryfield_player2 = tk.Entry(self.info_frame, width=25, state="readonly")
        self.entryfield_player2.grid(row=2, column=1, pady=5)

        # Current Player Turn
        self.label_game_record = tk.Label(self.info_frame, text="Current Turn", bg=self.bg_color1)
        self.label_game_record.grid(row=3, column=0, sticky='w', pady=5)
        self.entryfield_current_player_turn = tk.Entry(self.info_frame, width=25, state="readonly")
        self.entryfield_current_player_turn.grid(row=3, column=1, pady=(10, 20))  # Adds gap above and below
        
        # Game Win Record
        self.label_game_record = tk.Label(self.info_frame, text="Game Win Record", bg=self.bg_color1)
        self.label_game_record.grid(row=4, column=0, sticky='w', pady=5)
        self.textfield_game_record = tk.Text(self.info_frame, width=20, height=4, wrap=tk.WORD, state="normal")
        self.textfield_game_record.grid(row=4, column=1, pady=5)
        self.scrollbar_game_record = ttk.Scrollbar(self.info_frame, command=self.textfield_game_record.yview)
        self.scrollbar_game_record.grid(row=4, column=2, sticky='ns')  # 'ns' makes it stretch vertically
        self.textfield_game_record.config(yscrollcommand=self.scrollbar_game_record.set)

        # Current System Date
        self.label_current_date = tk.Label(self.info_frame, text="Current System Date", bg=self.bg_color1)
        self.label_current_date.grid(row=5, column=0, sticky='w', pady=5)
        self.entryfield_current_date = tk.Entry(self.info_frame, width=25, state="readonly")
        self.entryfield_current_date.grid(row=5, column=1, pady=5)

        # Current System Time
        self.label_current_time = tk.Label(self.info_frame, text="Current System Time", bg=self.bg_color1)
        self.label_current_time.grid(row=6, column=0, sticky='w', pady=5)
        self.entryfield_current_time = tk.Entry(self.info_frame, width=25, state="readonly")
        self.entryfield_current_time.grid(row=6, column=1, pady=5)

        # Button to stop game
        self._button_stop = tk.Button(self.root, text="QUIT", fg="red", bg=self.bg_color1, command=exit, width=12)
        self._button_stop.grid(row=7, column=0, sticky='w', padx=5, pady=5)


    def create_tic_tac_toe_board(self, button_func: Callable[[int], None], empty_mark: str) -> None:
        """This functions creates the tic-tac-toe board on the GUI."""
        self.buttons: list[tk.Button] = []
        for i in range(9):
            button = tk.Button(self.grid_frame, text=empty_mark, width=10, height=4, bg=self.bg_color2,
                               font=("TkDefaultFont", 12, "bold"), command=lambda pos=i: button_func(pos))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
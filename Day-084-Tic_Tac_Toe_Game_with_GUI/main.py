from tkinter import Tk, Canvas, Frame, Button, Label

# Global Variables
BACKGROUND_COLOR = "#C2FFC1"
GRID_COLOR = "#2D5A2C"
X_COLOR = "#343A40"
O_COLOR = "#E05353"
WIN_LINE_COLOR = "yellow"
TOTAL_CELL = 9
WINNING_SCORE = 5
PL1_CURRENT_SCORE = 0
PL2_CURRENT_SCORE = 0

player1_cell_list = []
player2_cell_list = []

# X Y COORDINATE LIST & SYMBOL CENTER COORDINATE LIST, (and each cell number for win condition checking)
x_axis_limit_list = [(0, 258, 1), (270, 523, 2), (536, 798, 3), (0, 258, 4), (270, 523, 5), (536, 799, 6), (0, 258, 7),
                     (270, 523, 8), (536, 798, 9)]
y_axis_limit_list = [(49, 258), (49, 258), (49, 258), (270, 475), (270, 475), (270, 475), (485, 689), (485, 689),
                     (485, 689)]
symbol_cord_list = [(130, 110), (392, 110), (666, 110), (130, 328), (392, 328), (666, 328), (130, 542), (392, 542),
                    (666, 542)]

# row, column, diagonal win condition
win_condition_dict = {
    "row_win_condition": [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}],
    "column_win_condition": [{1, 4, 7}, {2, 5, 8}, {3, 6, 9}],
    "diagonal_win_condition": [{1, 5, 9}, {3, 5, 7}, {None}]
}

# dictionary x0, y0, x1, y1 coordinate which will help in draw straight line if someone wins the game
winning_line_dict = {

    (1, 2, 3): [25, 105, 775, 105],
    (4, 5, 6): [25, 323, 775, 323],
    (7, 8, 9): [25, 535, 775, 535],

    (1, 4, 7): [130, 10, 130, 630],
    (2, 5, 8): [393, 10, 393, 630],
    (3, 6, 9): [667, 10, 667, 630],

    (1, 5, 9): [45, 35, 765, 615],
    (3, 5, 7): [755, 45, 25, 615],

}


class UserInterface(Tk):

    def __init__(self):
        super().__init__()

        window_width = 800
        window_height = 690

        # this will set the game window center to the screen.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.player2_symbol = None
        self.player1_symbol = None
        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y }")
        self.resizable(False, False)
        self.title("Tic Tac Toe")
        self.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

    def home_screen_ui(self):
        """this method will display the home screen UI"""

        def home_screen_btn(chosen_mode, game_mode_label):
            """this method will display button in home screen to show which symbol you wanna play with."""

            # this will destroy the old button on home screen so the symbol button can appear in their place.
            game_mode_canvas.itemconfig(game_mode_label, text="Choose Your Symbol")
            button_frame.destroy()
            friend_button.destroy()
            computer_button.destroy()

            # symbol button frame to create X and O button symbol
            symbol_btn_frame = Frame(self)
            symbol_btn_frame.config(bg=BACKGROUND_COLOR)
            symbol_btn_frame.grid(row=2, column=1, padx=0, pady=0)

            # creating X button
            x_button = Button(symbol_btn_frame, text="❌", width=11, height=1, font=("Roboto", 15, "bold"),
                              command=lambda: self.create_game_layout(chosen_mode, player1_symbol="X",
                                                                      player2_symbol="O"))
            x_button.pack(side='left', padx=20)

            # creating O button
            o_button = Button(symbol_btn_frame, text="⭕", width=11, height=1, font=("Roboto", 15, "bold"),
                              command=lambda: self.create_game_layout(chosen_mode, player1_symbol="O",
                                                                      player2_symbol="X"))
            o_button.pack(side='right', padx=20)

        # UI width and height with game title and other configuration
        title_canvas = Canvas(self, width=700, height=226)
        title_canvas.create_text(350, 113, text="❌ Tic Tac Toe ⭕", font=("Roboto", 60, "bold"))
        title_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        title_canvas.grid(row=0, column=1)

        # game_mode UI title and its configuration
        game_mode_canvas = Canvas(width=500, height=150)
        game_mode_title = game_mode_canvas.create_text(250, 70, text="Choose your opponent",
                                                       font=("Roboto", 30, "bold"))
        game_mode_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        game_mode_canvas.grid(row=1, column=1)

        # button frame to create computer and friend button
        button_frame = Frame(self)
        button_frame.config(bg=BACKGROUND_COLOR)
        button_frame.grid(row=2, column=1, padx=0, pady=0)

        self.game_mode = "friend"

        # button design details
        friend_button = Button(button_frame, text="Friend", width=11, height=1, font=("Roboto", 15, "bold"),
                               command=lambda: home_screen_btn(self.game_mode, game_mode_title))
        friend_button.pack(side='left', padx=20)

        self.game_mode = "computer"
        computer_button = Button(button_frame, text="Computer", width=11, height=1, font=("Roboto", 15, "bold"),
                                 command=lambda: home_screen_btn(self.game_mode, game_mode_title))
        computer_button.pack(side='right', padx=20)

        self.mainloop()

    def create_game_layout(self, chosen_mode, player1_symbol, player2_symbol):
        """this method will be responsible for creating game layout like game gridline and score section"""

        self.player1_symbol = player1_symbol
        self.player2_symbol = player2_symbol

        [widget.destroy() for widget in self.winfo_children()]  # removing all the previous screen widget
        self.config(padx=0, pady=0)

        # creating frame for Score label
        score_label_frame = Frame(self)
        score_label_frame.config(bg=BACKGROUND_COLOR)
        score_label_frame.grid(row=0, column=1, padx=0, pady=10)

        # creating left Score text label
        left_score_label = Label(score_label_frame, text=f"Player 1 Score: {PL1_CURRENT_SCORE}",
                                 font=("Arial", 14, "bold"),
                                 bg=BACKGROUND_COLOR)
        left_score_label.pack(side='left', padx=70)

        # creating VS label
        vs_label = Label(score_label_frame, text=f"VS", font=("Arial", 14, "bold"), bg=BACKGROUND_COLOR)
        vs_label.pack(side='left', padx=80)

        # creating Right Score text label
        right_score_label = Label(score_label_frame, text=f"Player 2 Score: {PL2_CURRENT_SCORE}",
                                  font=("Arial", 14, "bold"),
                                  bg=BACKGROUND_COLOR)
        right_score_label.pack(side='right', padx=70)

        # score horizontal line
        score_horizontal_line = Frame(self)
        score_horizontal_line.config(height=2, bg="black", relief="sunken")
        score_horizontal_line.grid(row=1, column=1, sticky="ew")

        # tic tac toe game grid line
        self.canvas_gameline = Canvas(self, width=800, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas_gameline.grid(row=2, column=1)

        # horizontal game line
        self.canvas_gameline.create_line(0, 215, 800, 215, fill=GRID_COLOR, width=10)
        self.canvas_gameline.create_line(0, 430, 800, 430, fill=GRID_COLOR, width=10)

        # vertical game line
        self.canvas_gameline.create_line(265, 0, 265, 700, fill=GRID_COLOR, width=10)
        self.canvas_gameline.create_line(530, 0, 530, 700, fill=GRID_COLOR, width=10)

        self.draw_symbol(chosen_mode, player1_symbol, player2_symbol)

    def draw_symbol(self, chosen_mode, player1_symbol, player2_symbol):
        """this method will be responsible for adding symbol on the each cell."""
        global TOTAL_CELL

        def screen_clicked(event):
            """this method will register click on screen so it can draw symbols"""

            global TOTAL_CELL

            # Get mouse coordinates relative to the game window instead of the clicked widget.
            x_cord = event.x_root - self.winfo_rootx()
            y_cord = event.y_root - self.winfo_rooty()

            # this for loop will help in checking x axis, y axis outer limit against the click if click is between those
            # x and y axis it will draw symbol otherwise it will going to draw symbol symbol_cord_list helps in position
            # the symbol to exact correct location on each clicked cell.
            for index, (x_axis, y_axis, symbol_cord) in enumerate(
                    zip(x_axis_limit_list, y_axis_limit_list, symbol_cord_list)):

                if x_axis[0] < x_cord < x_axis[1] and y_axis[0] < y_cord < y_axis[
                    1]:  # this if statement will check that x and y axis outer range that the click should be in between this coordinate

                    if TOTAL_CELL > 0:  # until the grid cell value is greater than 0 at that much time the game will run.

                        if TOTAL_CELL % 2 != 0:  # this condition helps in changing player turn to player 1
                            player1_cell_list.append(x_axis[2])
                            self.canvas_gameline.create_text(symbol_cord[0], symbol_cord[1], text=player1_symbol,
                                                             font=("Arial", 190), fill=X_COLOR)

                        elif TOTAL_CELL % 2 == 0:  # this condition helps in changing player turn to player 2
                            player2_cell_list.append(x_axis[2])
                            self.canvas_gameline.create_text(symbol_cord[0], symbol_cord[1], text=player2_symbol,
                                                             font=("Arial", 190), fill=O_COLOR)

                        TOTAL_CELL -= 1

                        # after each click it will remove the index of each x, y symbol coordinate axis so that when user
                        # clicks on the cell where already symbol present another symbol didnt get created.
                        x_axis_limit_list.pop(index)
                        y_axis_limit_list.pop(index)
                        symbol_cord_list.pop(index)

                        self.latest_cell_clicked()

        self.canvas_gameline.bind("<Button-1>", screen_clicked)

    def latest_cell_clicked(self):

        player1_cell_set = set()
        player2_cell_set = set()

        def create_player_set():

            if len(player1_cell_list) >= 3:
                player1_cell_set.update(player1_cell_list)

            if len(player2_cell_list) >= 3:
                player2_cell_set.update(player2_cell_list)

        create_player_set()
        self.check__round_winner(player1_cell_set, player2_cell_set)

    def check__round_winner(self, pl1_cell_set, pl2_cell_set):
        """this method is responsible for finding the winner."""

        player_won = False
        global PL1_CURRENT_SCORE, PL2_CURRENT_SCORE, CELL_FILL_COUNTER

        # this for select row, column, diagonal win condition  sets to compare with winner_set to find the winner one at a time.
        for row_set, col_set, diagonal_set in zip(win_condition_dict["row_win_condition"],
                                                  win_condition_dict["column_win_condition"],
                                                  win_condition_dict["diagonal_win_condition"]):

            current_conditions = (row_set, col_set, diagonal_set)

            for win_set in current_conditions:  # checks is winner set present in current cycle win condition

                if win_set <= pl1_cell_set:  # this condition checks winner set value is present or not in player 1 set
                    PL1_CURRENT_SCORE += 1

                    self.draw_win_line(win_set)
                    self.show_round_winner("🎉 Player 1 Won!")
                    player_won = True

                    break

                if win_set <= pl2_cell_set:  # this condition checks winner set value is present or not in player 2 set

                    PL2_CURRENT_SCORE += 1
                    self.draw_win_line(win_set)
                    self.show_round_winner("🎉 Player 2 Won!")
                    player_won = True

                    break

            if player_won:
                self.reset_board()

        # if both of the player didnt win the match and total cell count is 0 then this condition becomes True
        if TOTAL_CELL == 0 and player_won == False:
            round_winner = "This round is Draw!"
            self.show_round_winner(round_winner)
            self.reset_board()

    def draw_win_line(self, win_condition_set):
        """this method will be responsible for drawing the winner horizontal, vertical, diagonal line"""

        # this for loop helps in compare winner set with winner line dictionary set to find on which coordinate and for
        # which sets line should be drawn
        for winning_line_set in winning_line_dict:

            if win_condition_set == set(winning_line_set):

                # getting the coordinate to draw line from winning line dictionary
                x0_cord, y0_cord = winning_line_dict[winning_line_set][0], winning_line_dict[winning_line_set][1]
                x1_cord, y1_cord = winning_line_dict[winning_line_set][2], winning_line_dict[winning_line_set][3]

                if win_condition_set in win_condition_dict["row_win_condition"]:  # if winner set is row

                    self.canvas_gameline.create_line(x0_cord, y0_cord, x1_cord, y1_cord, fill=WIN_LINE_COLOR, width=15,
                                                     capstyle="round")
                    break

                elif win_condition_set in win_condition_dict["column_win_condition"]:  # if winner set is column

                    self.canvas_gameline.create_line(x0_cord, y0_cord, x1_cord, y1_cord, fill=WIN_LINE_COLOR, width=15,
                                                     capstyle="round")
                    break

                elif win_condition_set in win_condition_dict["diagonal_win_condition"]:  # if winner set is diagonal

                    if win_condition_set == {1, 5, 9}:

                        self.canvas_gameline.create_line(x0_cord, y0_cord, x1_cord, y1_cord, fill=WIN_LINE_COLOR,
                                                         width=15, capstyle="round")

                        break

                    elif win_condition_set == {3, 5, 7}:

                        self.canvas_gameline.create_line(x0_cord, y0_cord, x1_cord, y1_cord, fill=WIN_LINE_COLOR,
                                                         width=15, capstyle="round", )
                        break

    def show_round_winner(self, round_winner):
        """this method will show the round winner or draw message"""

        round_winner_canvas = Canvas(width=400, height=100, bg="white")
        round_winner_canvas.place(x=200, y=300)
        round_winner_canvas.create_text(200, 50, text=f"{round_winner}", font=("Roboto", 30, "bold"), fill="black",
                                        anchor="center")

    def reset_board(self):
        """this method will reset the board for the next round"""

        self.reset_game_variables()

        self.after(1500, lambda: self.create_game_layout(self.game_mode, self.player1_symbol, self.player2_symbol))
        self.after( 1500, self.check_match_winner)

    def check_match_winner(self):
        """this method checks who the match out of overall winning score. and display the match winner"""

        def display_match_winner(player, match_winner_score, match_losser_score):
            """this function display the match winner"""

            match_winner_canvas = Canvas(width=400, height=100, bg="white")
            match_winner_canvas.place(x=200, y=300)
            match_winner_canvas.create_text(200, 50,
                                            text=f" {player} 🎉\n    With the Score of {match_winner_score} - {match_losser_score}",
                                            font=("Roboto", 20, "bold"), fill="black",
                                            anchor="center")

            self.after(1500, self.rematch)
            self.wait_window()

        if PL1_CURRENT_SCORE == WINNING_SCORE:
            display_match_winner("Player 1 Won the Match", match_winner_score=PL1_CURRENT_SCORE,
                                 match_losser_score=PL2_CURRENT_SCORE)

        elif PL2_CURRENT_SCORE == WINNING_SCORE:
            display_match_winner("Player 2 Won the Match", match_losser_score=PL1_CURRENT_SCORE,
                                 match_winner_score=PL2_CURRENT_SCORE)


    def reset_game_variables(self):

        global TOTAL_CELL, player1_cell_list, player2_cell_list, x_axis_limit_list, y_axis_limit_list, symbol_cord_list

        TOTAL_CELL = 9
        player1_cell_list.clear()
        player2_cell_list.clear()

        self.canvas_gameline.unbind("<Button-1>")

        # X Y COORDINATE LIST & SYMBOL CENTER COORDINATE LIST, (and each cell number for win condition checking)
        x_axis_limit_list = [(0, 258, 1), (270, 523, 2), (536, 798, 3), (0, 258, 4), (270, 523, 5), (536, 799, 6),
                             (0, 258, 7),
                             (270, 523, 8), (536, 798, 9)]
        y_axis_limit_list = [(49, 258), (49, 258), (49, 258), (270, 475), (270, 475), (270, 475), (485, 689),
                             (485, 689),
                             (485, 689)]
        symbol_cord_list = [(130, 110), (392, 110), (666, 110), (130, 328), (392, 328), (666, 328), (130, 542),
                            (392, 542),
                            (666, 542)]

    def rematch(self):
        """this method is responsible for resetting the game so that new match get started and closing the game."""

        def reset_new_match():
            """this function will reset the new match by taking user to home screen."""

            global PL1_CURRENT_SCORE, PL2_CURRENT_SCORE
            PL1_CURRENT_SCORE, PL2_CURRENT_SCORE = 0, 0
            self.reset_game_variables()
            [widget.destroy() for widget in self.winfo_children()]  # removing all the previous screen widget
            self.config(padx=50, pady=50)
            self.home_screen_ui()

        def exit_game():
            """this function closes the game."""
            self.destroy()

        rematch_canvas = Canvas(width=400, height=150, bg="white")
        rematch_canvas.place(x=200, y=300)
        rematch_canvas.create_text(200, 50,
                                   text=f"Do you want to Play Again!",
                                   font=("Roboto", 20, "bold"), fill="black",
                                   anchor="center")

        yes_button = Button(rematch_canvas, text="Yes", command=reset_new_match, font=("Roboto", 15, "bold"),
                            bg=BACKGROUND_COLOR, width=8, height=1)
        yes_button.place(x=70, y=80)
        no_button = Button(rematch_canvas, text="No", command= exit_game, font=("Roboto", 15, "bold"),
                           bg=BACKGROUND_COLOR, width=8, height=1)
        no_button.place(x=220, y=80)


# creating instance for calling the home_screen ui method
user_interface = UserInterface()
user_interface.home_screen_ui()

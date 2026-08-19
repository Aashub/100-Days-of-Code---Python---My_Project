from tkinter import *
from tkinter.font import Font
from typing_data import typing_paragraph_dict
import random

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 600

TEXT_COLOR = "#666666"
BACKGROUND_COLOR = "#1E1E1E"
BUTTON_COLOR = "#FFC000"

fg_color_index = 0  # this variable keeps track of character position
START_TIMER = 0  # this variable makes a if condition true in check_retrieved_text method to call  timer_countdown method
STOP_TIMER_COUNTDOWN = False


class UserInterface(Tk):

    def __init__(self):

        super().__init__()

        # this will set the game window center to the screen.

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
        center_y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))

        self.selected_difficulty_mode = "easy_mode"
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")
        self.resizable(False, False)
        self.title("typing-speed-tester")
        self.app_font = Font(family="Segoe UI", size=16, slant="italic")

    # ********************************************** TYPING TEST SCREEN ************************************************

    def add_typing_test_screen(self):
        """this method add background image in home screen"""

        # add home screen image
        self.img = PhotoImage(file="img/bg.png")
        image_label = Label(self, image=self.img)
        image_label.pack()

    # ************************************************ WIDGET  BUTTON **************************************************

    def all_widget_button(self):

        # reset button
        self.reset_btn = Button(self, text="⭮", font=("Arial", 25, "bold"), fg=BUTTON_COLOR,
                                bd=0, bg=BACKGROUND_COLOR, height=1, width=3, command=self.reset_typing)
        self.reset_btn.place(x=510, y=480)

        # Create a shared Tkinter variable
        self.selected_option = StringVar(self, value="Option 1")

        #  Create the Radiobutton widgets
        easy_radio_btn = Radiobutton(self, text="Easy", variable=self.selected_option, value="easy_mode",
                                     bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                     activebackground=BACKGROUND_COLOR,
                                     activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                     command=self.handle_typing_mode
                                     )

        normal_radio_btn = Radiobutton(self, text="Normal", variable=self.selected_option, value="normal_mode",
                                       bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial",),
                                       activebackground=BACKGROUND_COLOR,
                                       activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                       command=self.handle_typing_mode
                                       )

        hard_radio_btn = Radiobutton(self, text="Hard", variable=self.selected_option,
                                     value="hard_mode",
                                     bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                     activebackground=BACKGROUND_COLOR,
                                     activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                     command=self.handle_typing_mode
                                     )

        # 3. Display the radio button on the screen
        easy_radio_btn.place(x=200, y=500)
        normal_radio_btn.place(x=300, y=500)
        hard_radio_btn.place(x=410, y=500)

        # Create a shared Tkinter variable
        self.timer_mode = StringVar(self, value="Option 1")

        #  Create the Radiobutton widgets
        self.second_60_btn = Radiobutton(self, text="60", variable=self.timer_mode, value="60, 60_seconds",
                                         bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                         activebackground=BACKGROUND_COLOR,
                                         activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                         )

        self.second_120_btn = Radiobutton(self, text="120", variable=self.timer_mode, value="120, 120_seconds",
                                          bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial",),
                                          activebackground=BACKGROUND_COLOR,
                                          activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                          )

        self.second_180_btn = Radiobutton(self, text="180", variable=self.timer_mode,
                                          value="180, 180_seconds",
                                          bg=BACKGROUND_COLOR, fg=BUTTON_COLOR, font=("Arial"),
                                          activebackground=BACKGROUND_COLOR,
                                          activeforeground="white", selectcolor=BACKGROUND_COLOR,
                                          )

        # 3. Display the radio button on the screen
        self.second_60_btn.place(x=620, y=500)
        self.second_120_btn.place(x=715, y=500)
        self.second_180_btn.place(x=820, y=500)

        # entry field
        self.entered_text_input = Text(self, font=("Arial", 30), width=10, height=1, relief="flat")
        self.entered_text_input.place(x=440, y=-50)
        self.entered_text_input.focus_set()

        # timer label
        seconds_left = None
        self.timer_text = Label(self, text=f"{seconds_left}", font=("Arial", 30), relief="flat", bg=BACKGROUND_COLOR,
                                fg=BUTTON_COLOR)

        # wpm label
        self.wpm_text = Label(self, text=f"WPM: ", font=("Arial", 30), relief="flat", bg=BACKGROUND_COLOR,
                              fg=BUTTON_COLOR)

    # ******************************************** ADD TYPING TEXT AREA ************************************************

    def display_typing_text(self):
        """this method display typing text on screen so that user can see whats needs to be typed."""

        self.display_text = Text(self, font=self.app_font, fg=TEXT_COLOR, height=10, width=70, wrap="word",
                                 bg=BACKGROUND_COLOR, bd=0, pady=15, padx=15)

        default_sentence_index = random.randint(0, 4)
        self.display_text.insert("1.0", typing_paragraph_dict["easy_mode"][default_sentence_index])
        self.display_text.place(x=145, y=130)

    def check_retrieved_text(self, event):
        """this method will check user entered text vs typing text and highlight character with white color if correct and red if wrong character"""

        global fg_color_index, START_TIMER, STOP_TIMER_COUNTDOWN

        STOP_TIMER_COUNTDOWN = False

        if not STOP_TIMER_COUNTDOWN:
            self.timer_text.place(x=510, y=80)

        # gets text input and gets display typing text display text.
        text_input = self.entered_text_input.get("1.0", "end-1c")
        self.display_text_string = self.display_text.get("1.0", "end-1c")

        if START_TIMER == 0:
            timer_mode = self.timer_mode.get().split()

            try:
                self.total_seconds = int(timer_mode[0].replace(",", ""))
                selected_timer_option = timer_mode[1]
                self.timer_countdown(self.total_seconds, selected_timer_option)

            except ValueError:

                self.total_seconds = 60
                selected_timer_option = "60_seconds"
                self.timer_countdown(self.total_seconds, selected_timer_option)

        # ignores the shift Left side btn while using
        if event.keysym == ("Shift_L"):
            return

        # when user press backspace this if statement will help in backwords to correct a sentence.
        if event.keysym == ("BackSpace"):
            fg_color_index -= 1
            tag_name = f"char_{fg_color_index}"

            # here we are getting the fg_color of the character which needs to be corrected
            fg_color = self.get_foreground_at_index(self.display_text, f"1.{fg_color_index}")

            # character color is white and red it will reassign that character color to original text color which will help user to navigate at which position he is currently in.
            if fg_color == "white" or fg_color == "red":
                self.display_text.tag_config(tag_name, foreground=TEXT_COLOR)
                self.display_text.tag_add(tag_name, f"1.{fg_color_index}")

            return

        # this method will give the current text color so that it will update the text color if not filled gives white color, if filled with red & white color than gives red & white color
        fg_color = self.get_foreground_at_index(self.display_text, f"1.{fg_color_index}")

        # this for loop checks the user input char and typing text char and change color based on match and mismatch.
        for char_index, (display_char, input_char) in enumerate(zip(self.display_text_string, text_input)):

            if fg_color == TEXT_COLOR:

                tag_name = f"char_{char_index}"  # unique tag per position

                if self.display_text_string[char_index] == input_char:
                    self.display_text.tag_config(tag_name, foreground="white")

                elif self.display_text_string[char_index] != input_char:

                    self.display_text.tag_config(tag_name, foreground="red")
                self.display_text.tag_add(tag_name, f"1.{char_index}")

        fg_color_index += 1
        START_TIMER += 1

    def get_foreground_at_index(self, text_widget, index):
        """this method will give us the current text character of typing text, text color for checking."""

        tags_at_index = text_widget.tag_names(index)

        for tag in tags_at_index:
            fg_color = text_widget.tag_cget(tag, "foreground")
            if fg_color:
                return fg_color

        #  Fallback to the text widget's global default foreground configuration
        return text_widget.cget("foreground")

    # *************************************** timer Countdown functionality ********************************************

    def timer_countdown(self, seconds_left, selected_timer_option):
        """this method starts the countdown when user starts typing and stops the time when """

        global count_second
        self.timer_text.config(text=seconds_left)
        self.timer_text.place(x=510, y=80)

        if selected_timer_option == "60_seconds":
            count_second = seconds_left % 60
        elif selected_timer_option == "120_seconds":
            count_second = seconds_left % 120
        elif selected_timer_option == "180_seconds":
            count_second = seconds_left % 180

        # this if statement will help in bypassing the issue of when seconds are left less than 10 so it will show then as an 09 08 and so on
        if count_second == 0:

            count_second = seconds_left
            if count_second == 0:
                self.timer_text.place_forget()
                self.entered_text_input.config(state="disabled")
                self.calculate_word_per_minute()
                return

        elif count_second < 10:
            count_second = f"0{count_second}"

        self.timer_text.config(text=f"{count_second}")

        # if the condition of STOP_TIMER_COUNTDOWN became True than it will stop the timer_countdown method.
        if STOP_TIMER_COUNTDOWN:
            self.timer_text.place_forget()
            return

        # if seconds will be greater than 0 than .after() method will call the time_countdown function again & also subtract the second each second.
        if seconds_left > 0:
            self.after(600, self.timer_countdown, seconds_left - 1, selected_timer_option)

    # ************************************* calculate wpm & keystroke accuracy******************************************

    def calculate_word_per_minute(self):
        """this method calculate and show word per minute user has achieved."""

        # getting all entered text in list format for total word count.
        all_input_word_list = self.entered_text_input.get("1.0", "end-1c").split()
        displayed_word_list = self.display_text_string.split()

        # gives total word count if all the typed word is correct
        total_word_count = len(all_input_word_list)

        # gives total word count of typed word including incorrect.
        if all_input_word_list[total_word_count - 1] != displayed_word_list[total_word_count]:
            total_word_count -= 1

        total_minutes = self.total_seconds / 60  # calculating seconds in minute

        word_per_minute = int(round(total_word_count / total_minutes, 0))

        self.wpm_text.config(text=f"WPM: {word_per_minute}")
        self.wpm_text.place(x=455, y=70)

    # ************************************************ Reset Typing  ***************************************************

    def reset_typing(self):
        """this method will rest the typing so when user click on rest btn everything gets reset so that user can restart typing."""

        global fg_color_index, START_TIMER, STOP_TIMER_COUNTDOWN, count_second

        default_typing_mode = self.selected_option.get()

        if default_typing_mode == "Option 1":
            random_index = random.randint(0, 4)
            self.display_text.delete('1.0', 'end')
            sentence = typing_paragraph_dict["easy_mode"][random_index]
            self.display_text.insert("1.0", sentence)

        else:
            # reset the global variable back to zero
            fg_color_index = 0
            START_TIMER = 0
            STOP_TIMER_COUNTDOWN = True

            # clear the user's typed input and make state normal so that user can start new typing.
            self.entered_text_input.config(state="normal")
            self.entered_text_input.delete("1.0", "end")

            # reset all character highlighting back to the default color
            # remove all the per-character tags we created during the test
            for tag in self.display_text.tag_names():
                if tag.startswith("char_"):
                    self.display_text.tag_delete(tag)

            # make word_per_minute text disappear
            self.wpm_text.place_forget()

            # make timer text disappear
            self.timer_text.place_forget()

    # ******************************************** Set Difficulty Mode *************************************************

    def handle_typing_mode(self):
        """this method will update the sentence as per the selected difficulty leve."""

        if self.selected_option.get():

            self.reset_typing()
            self.selected_difficulty_mode = self.selected_option.get()
            self.display_text.delete('1.0', 'end')

            random_index = random.randint(0, 4)
            for difficulty_mode in typing_paragraph_dict:

                if difficulty_mode == self.selected_difficulty_mode:
                    sentence = typing_paragraph_dict[difficulty_mode][random_index]
                    self.display_text.insert("1.0", sentence)
                    break

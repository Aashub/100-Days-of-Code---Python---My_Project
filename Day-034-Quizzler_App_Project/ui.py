from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")
SCORE = 0

class QuizInterface:

    def __init__(self, quiz_question, quiz_answer, quiz_object):
        """this init method will create a UI interface for the app."""

        self.quiz_object = quiz_object
        self.quiz_answer = quiz_answer
        self.quiz_question = quiz_question

        # window
        self.window = Tk()
        self.window.title("Quizzler",)
        self.window.resizable(False, False)
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)

        # button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command= self.true_button_clicked)
        self.true_button.grid(row=2, column=0, padx=20, sticky="w")
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command= self.false_button_clicked)
        self.false_button.grid(row=2, column=1, padx=20, sticky="e")

        self.question_text()
        self.score()
        self.window.mainloop()

    def question_text(self):
        """this method will show the question text each time this method get called"""

        self.question_label = Label(text=self.quiz_question, font=FONT)
        self.question_label.config(wraplength=300, height=10, width=27)
        self.question_label.grid(column=0, row=1, columnspan=2, pady=30)

    def score(self):
        """this method will show updated score each time this method get called."""

        self.score_label = Label(text= f"Score: {SCORE}", font=("Arial", 15, "bold"), bg = THEME_COLOR, fg= "white")
        self.score_label.grid(column=1, row=0, columnspan=2, pady=20, sticky="e")

    def true_button_clicked(self):
        """this method will call check_answer method in quiz_brain class and give us return value True or False and than also call give_feedback method"""

        user_answer = "true"
        is_right = self.quiz_object.check_answer(user_answer, self.quiz_answer)
        self.give_feedback(is_right)

    def false_button_clicked(self):
        """this method will call check_answer method in quiz_brain class and give us return value True or False and than also call give_feedback method"""

        user_answer = "false"
        is_right = self.quiz_object.check_answer(user_answer, self.quiz_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """this method will update the score each time correct answer register and change the question label color and also call get_next_question"""

        global SCORE
        if is_right:
            self.question_label.config(bg="green")
            SCORE += 1
        else:
            self.question_label.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        """this method check that do we have any question by calling quiz_brain class still_has_question"""

        self.question_label.config(bg= "white")
        if self.quiz_object.still_has_question():
            quiz_question, quiz_answer = self.quiz_object.next_question()
            self.quiz_question = quiz_question
            self.quiz_answer = quiz_answer
            self.score()
            self.question_text()

        else:
            self.quiz_question = "You've have reached the end of the question!"
            self.question_label.config(text= self.quiz_question)
            self.question_text()
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        self.question_text()

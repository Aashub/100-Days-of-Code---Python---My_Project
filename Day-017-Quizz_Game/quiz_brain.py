class QuizzBrain:

    def __init__(self,question_list):

        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        """this method will check that question list have more question and return true or false value"""

        if len(self.question_list) != self.question_number:
            return True
        else:
            return False

    def next_question(self):
        """this method will ask the user the next question"""

        # below line was creating object of each class which we have stored in a question list.
        question_object = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_object.text} (True/False)? :").lower()
        question_object.answer.lower()

        self.check_answer(user_answer, question_object.answer)

    def check_answer(self, u_answer, correct_answer):
        """this method will check that answer is correct or not and as per that give us output."""

        if u_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("You are wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")

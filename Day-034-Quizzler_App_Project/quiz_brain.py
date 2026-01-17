import html

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
        """this method will get the question from question list and return its question and correct answer value"""

        # below line was creating object of each class which we have stored in a question list.
        question_object = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(question_object.text)
        question = f"Q.{self.question_number}: {q_text}"
        correct_answer = question_object.answer

        return question, correct_answer

    def check_answer(self, u_answer, correct_answer):
        """this method will check that answer is correct or not and as per that give us output."""

        if u_answer == correct_answer.lower():
            self.score += 1
            return True

        else:
            return False
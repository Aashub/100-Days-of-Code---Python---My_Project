from question_model import Question
from data import question_data
from quiz_brain import  QuizzBrain
from ui import QuizInterface
question_bank = []

# this for loop will append each classes created of question and answer data and append them in question bank list
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizzBrain(question_bank)

# here we are next_question() method to get the next question each time it will be called.
quiz_question, quiz_answer = quiz.next_question()

# here we are giving the quiz question, answer and quiz object so that we can call show the question on the UI and do other functionality
quiz_ui = QuizInterface(quiz_question, quiz_answer, quiz)



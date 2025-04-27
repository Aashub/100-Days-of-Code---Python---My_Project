from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# this for loop will create object and store all the question and answer object in a list(question bank)
for to_store_question in question_data:
    new_question = Question(to_store_question["question"], to_store_question["correct_answer"])

    question_bank.append(new_question)

#this object will take question_bank input and store it into the question_list attribute in a QuizBrain class
ask_question = QuizBrain(q_list=question_bank)

# here we are calling one of the method o Quiz brain so we can iterate to next question and also find out the answer and
# and their total score.
ask_question.next_question(ask_question.question_list, ask_question.question_number)







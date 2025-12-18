from question_model import Question
from data import question_data
from quiz_brain import  QuizzBrain

question_bank = []

# this for loop will append each classes created of question and answer data and append them in question bank file
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quizz = QuizzBrain(question_bank)

# this whiile loop will run until still_has_question() method don't return False
while quizz.still_has_question():
    quizz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizz.score}/{quizz.question_number}")



class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self, ques_ans_details, question_num):
        """this function will iterate to next question &
        check that user has provided correct answer or not or as per his input it will show so result."""

        score = self.score

        should_continue = True
        while should_continue:
            #here we will iterate the loop until the user don't complete the all quiz questions.
            if len(ques_ans_details) > question_num:
                current_question = ques_ans_details[question_num]

                question = current_question.text
                answer = current_question.answer
                asked_question = input(f"Q.{question_num+1}: {question}, (True/False)? ").capitalize()

                #this if else statement block will check that user has provided correctinput or not.
                if asked_question == answer:
                    question_num += 1
                    score += 1

                    print(f"You got it right!\nThe correct answer was: {answer}")

                elif asked_question != answer and asked_question == "True" or asked_question == "False":
                    question_num += 1
                    print("That's wrong.")

                else:
                    print("Invalid Input, Please provide correct input!")

                print(f"Your current score is {score}/{question_num}\n\n")

            else:
                print(f"you have completed the Quiz.\nYour final score is {score}/{question_num} ")
                exit()






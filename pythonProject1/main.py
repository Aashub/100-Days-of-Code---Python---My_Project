# name = "Ashish"
# new_name = [letter for letter in name]
#
# print(new_name)

# my_list = [double*2 for double in range(1,5)]
#
# print(my_list)

import  random

names = ["dogisj", "dgosi", "gowierg", "vjowegia", "gwoieg", "goiaa"]

student_score = {score:random.randint(1,100) for score in names}

print(student_score)
passed_student = {passed:student_score[passed] for passed in student_score if student_score[passed] > 60}

print(passed_student)
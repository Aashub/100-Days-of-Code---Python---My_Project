from binstar_client.pprintb import user_list
from docutils.utils.math.latex2mathml import letters

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_details = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in nato_details.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


user_input = input("Enter a word: ").upper()
new_list = [new_dict[char] for char in user_input if char in new_dict]

print(new_list)




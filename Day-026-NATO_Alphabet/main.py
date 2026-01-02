import pandas

# reading a csv file using pandas module
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# creating a dictionary of letter as key and code as their value using dictionary comprehension
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

user_input = input("enter a word: ").upper()

# creating a phonetic code list using list comprehension of each letter of user input.
phonetic_list = [phonetic_dict[char] for char in user_input if char in phonetic_dict[char]]

print(phonetic_list)
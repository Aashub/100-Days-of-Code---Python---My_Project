import pandas

# here we are reading the csv file by using pandas module so we can retreive the data
nato_details = pandas.read_csv("nato_phonetic_alphabet.csv")

# here we are creting a dictionary using dictionary comprehension which where each letter will contain its NATO code example(A" Alpha)
new_dict = {row.letter:row.code for (index, row) in nato_details.iterrows()}


user_input = input("Enter a word: ").upper()

# here we are creating a new list which will contain a NATO code of each alphabet character which was given by usre
new_list = [new_dict[char] for char in user_input if char in new_dict]

print(new_list)




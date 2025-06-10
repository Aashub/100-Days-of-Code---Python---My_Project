
#empty list to store /n removed names
name_list = []

# here we are reading the file of starting_letter
with open("./Input/Letters/._starting_letter.txt") as starting_letter:
    draft_letter = starting_letter.read()

    #from the invited_names file we are reading here each line and storing its value in "name"
    names = open("./Input/Names/._invited_names.txt")
    name = names.readlines()

    # by using for loop we have appended the invited names in name_list and stripping "/n" which is making difficult to
    #read or write the file
    for name_of_list in name:
        name_list.append(name_of_list.strip())
    names.close()

    # here we have created a new files for the invited names so we can create a letter.
    for creating_files in name_list:
        with open(f"./Output/ReadyToSend/{creating_files}.txt", "w") as created_files:
            file = created_files.write(draft_letter)

    for named_letter in name_list:

        # here we are opening the newly created letter in read mode so we replace the "name" with invited names
        with open(f"./Output/ReadyToSend/{named_letter}.txt", "r") as new_files:
            file_name = new_files.read()
            new = file_name.replace("[name]", named_letter)

        # here we are opening the newly created letter in write mode so the invited names will updated in each file
        with open(f"./Output/ReadyToSend/{named_letter}.txt", "w") as updated_files:
            new_file = updated_files.write(new)


















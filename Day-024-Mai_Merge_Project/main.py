def create_namelist():
    """this method will create a name list with a stripped name and return a stripped name list."""

    name_list = []
    stripped_name = []

    # here we are reading a invited_names txt file by each line.
    with open(file="./Input/Names/invited_names.txt", mode= "r") as data:

        for each_line in range(8):
            name_data = data.readline()
            name_list.append(name_data)

    # here we are stripping a "\n" from a name_list
    for stripping_name in name_list:

        name = stripping_name.strip("\n")
        stripped_name.append(name)

    return stripped_name


def create_letter(names):
    """this method will create actual letter which we can send."""

    # here we are reading a starting_letter.txt file.
    with open(file= "./Input/Letters/starting_letter.txt", mode= "r") as letter:
        letter_format = letter.read()

    # this for loop will replace [name] with the name of sending person name.
    for name in names:
        new_letter = letter_format.replace("[name]", name)

        # here we are writing a letter and creating a txt file with the person name.
        with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
            letter.write(new_letter)

name_data = create_namelist()
create_letter(name_data)













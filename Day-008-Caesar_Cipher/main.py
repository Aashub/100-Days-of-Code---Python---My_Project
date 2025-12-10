from art import logo
print(logo)

# this function is work as to first time start the program.
def restart_caesar():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # this function will take all the necessary input and create encoded and decoded message
    def caesar(encoding_or_decoding, original_text, shift_number):

        encryption_decryption_list = []
        encoded_decoded_text = ""

        # this for loop will convert the original text into character list
        for char in original_text:
            encryption_decryption_list.append(char)

        # this for loop will check give us the encoded and decoded text
        for text_letter in encryption_decryption_list:
            # this if loop check that each character of list text is being present in alphabet list or not.
            if text_letter in alphabet:

                for alpha_letter in alphabet:

                    # this if statement will check that each letter of text list is matching with alphabet letter or not and if does match than it will do the enter this statement
                    if alpha_letter == text_letter:

                        if encoding_or_decoding == "encode":

                            #here we are getting an index number for encoded text
                            encode_index = (alphabet.index(alpha_letter) + shift_number) % len(alphabet)
                            encoded_decoded_text += alphabet[encode_index]

                        elif encoding_or_decoding == "decode":

                            # here we are getting an index number for decoded text
                            decode_index = (alphabet.index(alpha_letter) - shift_number) % len(alphabet)
                            encoded_decoded_text += alphabet[decode_index]


            # this elif statement will implement if any character not present in the alphabet list and that letter will added in the text as it is.
            elif text_letter not in alphabet:
                encoded_decoded_text += text_letter

        print(f"Here is the {encoding_or_decoding}d result: {encoded_decoded_text}")

        # here we are asking user to does he want to continue or not.
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

        # here we are using an recursion so that user can restart the program again and again until he doesn't want to stop
        if restart == "yes":
            restart_caesar()

        elif restart == "no":
            print("Good Bye")
            exit()

    caesar(encoding_or_decoding=direction, original_text=text, shift_number=shift)

restart_caesar()

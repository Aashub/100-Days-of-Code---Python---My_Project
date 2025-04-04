from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_length = len(alphabet)

"""this function will start the caesar cipher"""
def caesar_cipher():

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    """this function will encode the message"""
    def encrypt(original_text, shift_amount):

        encrypted_string = ""

        # by using modular operator on (alpha_index & shift_amount) & alphabet_length we get the remainder value
        # which we can use as index value to encrypted letter.
        for letter in original_text:

            # this if statement handle the problem if user have putted any symbol, number, which is not
            # present in alphabet list.
            if letter not in alphabet:
                encrypted_string += letter

            else:
                alpha_index = alphabet.index(letter)
                encrypted_index = (alpha_index + shift_amount) % alphabet_length
                if alphabet[alpha_index] == letter:
                    encrypted_string += alphabet[encrypted_index]

        print(f"Here's the encoded text: {encrypted_string}")
        return encrypted_string

    """this function will decode the message"""
    def decrypt(original_text, shift_amount):
        decrypted_string = ""

        # by using modular operator on (alpha_index & shift_amount) & alphabet_length we get the remainder value
        # which we can use as index value to decrypt letter.
        for letter in original_text:

            # this if statement handle the problem if user have putted any symbol, number, which is not
            # present in alphabet list.
            if letter not in alphabet:
                decrypted_string += letter

            else:
                alpha_index = alphabet.index(letter)
                decrypted_index = (alpha_index - shift_amount) % alphabet_length
                if alphabet[alpha_index] == letter:
                    decrypted_string += alphabet[decrypted_index]


        print(f"Here's the decoded result: {decrypted_string}")
        return decrypted_string

    """here the encrypt and decrypt function will be called."""
    if direction == "encode":
        encrypt(original_text = text, shift_amount = shift)

    elif direction == "decode":
        decrypt(original_text = text, shift_amount = shift)

    exit_cipher = input("Type yes if you want to go again. Otherwise type no.").lower()
    if exit_cipher == "yes":
        caesar_cipher()

    elif exit_cipher == "no":
        print("Goodbye")


caesar_cipher()

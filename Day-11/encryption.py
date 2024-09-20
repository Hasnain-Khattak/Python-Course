# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#
# text = input("Type your message: ").lower()
# shift = int(input("Type the shift number: "))
#
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
#
# def encrypt(text_input, shift_amount):
#     encrypted_text = ""
#     for letter in text_input:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         encrypted_text += alphabet[new_position]
#     print(encrypted_text)
#
#
# encrypt(text_input=text, shift_amount=shift)

# ----------------------------------------------------------------------------------------


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(input_text, shift_amount):
    encrypted_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        encrypted_text += alphabet[new_position]
    print(f"The encoded text is {encrypted_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(input_text, shift_amount):
    decrypet_text = ''
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount

        decrypet_text += alphabet[new_position]
    print(decrypet_text)



# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(input_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(input_text=text, shift_amount=shift)
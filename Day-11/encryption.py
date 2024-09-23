alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
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


def decrypt(input_text, shift_amount):
    decrypet_text = ''
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount

        decrypet_text += alphabet[new_position]
    print(decrypet_text)


if direction == 'encode':
    encrypt(input_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(input_text=text, shift_amount=shift)

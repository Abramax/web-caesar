def rotate_character(char, rot):
    return_string = ""
    position_num = alphabet_position(char)
    new_Position = ((position_num + rot)%26)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alphabet.upper()

    if char in alphabet:
        return_string += alphabet[new_Position]
        return return_string
    elif char in alpha_upper:
        return_string += alpha_upper[new_Position]
        return return_string
    else:
        return char


def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_length = len(alphabet)
    alpha_upper = alphabet.upper()
    position_num = 0
    for index in range(alpha_length):
        if letter == alphabet[index] or letter == alpha_upper[index]:
            position_num = index
    return position_num


def encrypt(text, rot):
    new_text = ""
    for letter in text:
        new_text = new_text + rotate_character(letter, rot)
    return new_text

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
        '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }
    morse_code_og = []
    invalid_chars = []

    for char in text.upper():
        if char == ' ':
            morse_code_og.append(' ')
        elif char in morse_code_dict:
            morse_code_og.append(morse_code_dict[char])
        else:
            invalid_chars.append(char)

    if invalid_chars:
        invalid_chars_str = ", ".join(invalid_chars)
        return f"Invalid character(s) in input: {invalid_chars_str}"

    return ' '.join(morse_code_og)


# Function Morse code to text
def morse_to_text(code):
    morse_code_dict_2 = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
        '-....-': '-', '-.--.': '(', '-.--.-': ')'
    }
    text = []
    morse_symbols = code.split(' ')
    consecutive_spaces = 0  # Track consecutive spaces

    for symbol in morse_symbols:
        if symbol == '':
            consecutive_spaces += 1
            if consecutive_spaces == 2:  # Single space
                text.append(' ')
                consecutive_spaces = 0
        else:
            if consecutive_spaces >= 1:  # Previous symbol(s) were space(s)
                text.append(' ')  # Add a single space
            consecutive_spaces = 0  # Reset consecutive spaces count
            if symbol in morse_code_dict_2:
                text.append(morse_code_dict_2[symbol])
            else:
                # Handle invalid Morse code patterns
                invalid_morse_pattern = handle_invalid_morse_pattern()
                text.append(invalid_morse_pattern)

    return ''.join(text)


def handle_invalid_morse_pattern():
    return 'INVALID'


def start():
    while True:
        user_input = input("type 'E' to encrypt or 'D' to decrypt: ").upper()

        if user_input == 'E':
            user_input_str = input("Enter a string to convert to Morse code: ")
            morse_code = text_to_morse(user_input_str)
            if 'Invalid character' in morse_code:
                print(f"Error: {morse_code}")
            else:
                print(f"Morse Code for '{user_input_str}': {morse_code}")
        elif user_input == 'D':
            morse_code = input("Enter Morse code to decrypt: ")
            decrypted_text = morse_to_text(morse_code)
            print(f"the Decrypted Text of: {morse_code} is {decrypted_text}")
        else:
            print("You can only enter letter 'E' or 'D'... Please try again")

        ask = input("Do you want to convert again? Enter 'Y' or 'N': ").upper()
        if ask != "Y":
            print("Thanks for using the Morse code converter :)")
            break


if __name__ == "__main__":
    start()

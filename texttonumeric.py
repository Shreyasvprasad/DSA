def sentence_to_keypad_sequence(sentence):
    keypad_mapping = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    keypad_sequence = ''
    sentence = sentence.upper()  # Convert the sentence to uppercase for mapping

    for char in sentence:
        if char in keypad_mapping:
            keypad_sequence += keypad_mapping[char]
        elif char == ' ':
            keypad_sequence += '0'  # Add '0' for space
        else:
            keypad_sequence += char  # If character is not in mapping, keep it as is

    return keypad_sequence

# Example usage
sentence = "Hello World"
keypad_sequence = sentence_to_keypad_sequence(sentence)
print("Keypad Sequence:", keypad_sequence)

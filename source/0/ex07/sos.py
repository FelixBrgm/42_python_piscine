import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def is_alphanumeric_with_spaces(string):
    """
    Checks if the string consits of nothing other than \
        alphanumeric characters and spaces
    """
    for char in string:
        if not (char.isalpha() or char.isdigit() or char.isspace()):
            return False
    return True


def convert_str_to_morsecode(text: str):
    """
    Converts a string into morsecode.
    The string has to consist of a combination of A-Z, a-z, 0-9 or ' '
    """
    if not is_alphanumeric_with_spaces(text):
        assert False,  "the arguments are bad"

    message = ""
    for i, letter in enumerate(text.upper()):
        message += NESTED_MORSE[letter]
        if i != len(text) - 1:
            message += " "

    return message


def sos():
    """
    Gets arguments from the command line and throws an "Assertationerror: \
        the arguments are bad" if not 1 argument is give or when it is \
            not a alphanumeric string with spaces
    """

    argv = sys.argv
    argc = len(argv)

    if argc != 2:
        assert False, "the arguments are bad"

    text = argv[1]

    if not isinstance(text, str):
        assert False, "the arguments are bad"

    print(convert_str_to_morsecode(text))


def main():
    """
    Executes sos and catches Assertationerros
    """
    try:
        sos()
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()

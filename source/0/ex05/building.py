import sys


def main():
    """
    Executes the building function an catches and prints AssertationErrors
    """
    try:
        building()
    except AssertionError as e:
        print("AssertionError:", e)


def building():
    """
    Takes a string from the commandline arguments and counts \
        different aspects of the string like
    - uppercase characters
    - lowercase characters
    - punctuation characters
    - space characters
    - digit characters
    and prints them.

    If more than 1 argument is provided a "AssertionError: more \
        than one argument is provided" is thrown.
    If no argument is provided the user is prompted to give on \
        via the command line.
    """
    argv = sys.argv
    argc = len(argv)

    if argc > 2:
        assert False, "more than one argument is provided"

    sentence = ""
    if argc == 1:
        sentence = input("What is the text to count?\n")
    else:
        sentence = argv[1]

    punctuation_posibilities = ".,;:!?\"-"

    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for letter in sentence:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif letter in punctuation_posibilities:
            punctuation += 1
        elif letter.isspace():
            spaces += 1
        elif letter.isdigit():
            digits += 1

    print("The text contains", len(sentence), "characters")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


if __name__ == "__main__":
    main()

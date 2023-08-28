from ft_filter import ft_filter
import sys


def cli_filter():
    """
    This function gets the commandline arguments for sentence: str and \
        min_len: int
    and splits the sentence and gives back an array of all words that \
        are over min_len.

    If a wrong number of arguments is given a "AssertationError: \
        the arguments are bad" is thrown"
    If the sentence is not a string and min_len is not a int a \
        "AssertationError: the arguments are bad" is thrown"

    Example:
        python script.py "Hello from world" 4 | cat -e
        $>["Hello", "World"]$
    """
    argv = sys.argv
    argc = len(argv)

    if argc != 3:
        assert False, "the arguments are bad"

    sentence = argv[1]
    min_len_str = argv[2]

    if not isinstance(sentence, str) or not min_len_str.isdigit():
        assert False, "the arguments are bad"

    min_len = int(min_len_str)
    print(ft_filter(sentence, min_len))


def main():
    """
    It calls cli_filter and prints errors that occour
    """
    try:
        cli_filter()
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()

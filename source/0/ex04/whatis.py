import sys

def main():
    try:
        whatis()
    except AssertionError as e:
            print("AssertionError:", e)

def whatis():
    argv = sys.argv
    argc = len(argv)

    if argc != 2:
        assert False, "more than one argument is provided"
    argument = argv[1]
    if not argument.isdigit():
        assert False, "argument is not an integer"

    number = int(argument)
    if number % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")

if __name__ == "__main__":
    main()
# Because we are not allowed external imports I
# have to use a default value
# if the terminal is smaller than this value you will have weird behaviour
DEFAULT_TERMINAL_WIDTH = 50


def ft_tqdm(lst: range) -> None:
    lst = range(len(lst))  # Normalises negative ranges

    length = len(lst)
    for e in lst:
        percentage = int(100 * ((e+1)/(length)))
        text = "{:3}%|".format(percentage)

        loading_bar_width_filled = \
            int((DEFAULT_TERMINAL_WIDTH * percentage/100))
        text += '█' * loading_bar_width_filled

        loading_bar_width_empty = \
            DEFAULT_TERMINAL_WIDTH - loading_bar_width_filled
        text += ' ' * loading_bar_width_empty

        text += '| '
        text += "{:len(str(length))}".format(e + 1)
        text += "/"
        text += str(len(lst))
        print(text)
        print("\033[F", end="")
        yield

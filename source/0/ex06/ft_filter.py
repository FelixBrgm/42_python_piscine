def ft_filter(sentence: str, min_len: int) -> []:
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable \
        for which function(item)
    is true. If function is None, return the items that are true.
    """
    words = []

    words = sentence.split(" ")

    # lambda functions basicly but a expression into a name \
    # tho they themselve are anonymous

    # [expression, item, iteratable, OPTIONAL condition] expression \
    # is to change items like a * 4

    words = [word for word in words
             if (lambda word, min_len: len(word) > min_len)(word, min_len)]

    return words

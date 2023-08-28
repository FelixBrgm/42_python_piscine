def ft_filter(sentence: str, min_len: int) -> []:
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable \
        for which function(item)
    is true. If function is None, return the items that are true.
    """
    words = []

    words = sentence.split(" ")

    words = [word for word in words if len(word) > min_len]

    return words

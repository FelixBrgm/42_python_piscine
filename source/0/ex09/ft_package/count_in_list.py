def count_in_list(lst, item):
    """
    Counts the amount of a item in a list and returns it
    """
    count = 0
    for e in lst:
        if e == item:
            count += 1
    return count

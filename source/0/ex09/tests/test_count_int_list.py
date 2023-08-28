from ft_package.count_in_list import count_in_list


def test_count_in_list():
    """
    Tests the count_int_list function and asserts when something is wrong
    """
    assert count_in_list(["toto", "tata", "toto"], "toto") == 2
    assert count_in_list(["toto", "tata", "toto"], "tutu") == 0

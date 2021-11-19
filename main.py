def test_function(string_to_print: str):
    """
    This is a test function for TravisCI. Prints the input string.
    :param string_to_print: string to print
    :return: none

    >>> test_function("test1")
    test1

    >>> test_function("test2")
    test2

    >>> test_function("test3")
    test3
    """
    print(string_to_print)


if __name__ == '__main__':
    test_function("Travis CI Setup")
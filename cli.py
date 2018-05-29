import sys


def parse_argv():
    """
    parse system arguments

    :return: Dict
    """

    # init options dict
    options = {}

    # loop through arguments
    for argument in sys.argv[1:]:
        # if option found
        if argument[:2] == '--':
            # get separator position
            separator = argument.find('=')

            # if is flag usage
            if separator == -1:
                options[argument[2:]] = True

            # if is params usage
            else:
                options[argument[2:separator]] = auto_convert(argument[separator + 1:])

    return options


def boolify(string):
    """
    convert string to boolean type

    :param string: string
    :return: bool
    """

    if string == 'True' or string == 'true':
        return True
    if string == 'False' or string == 'false':
        return False
    raise ValueError("wrong type")


def auto_convert(string):
    """
    convert string to corresponding type

    :param string: string
    :return: bool|int|float|string
    """

    for fn in (boolify, int, float):
        try:
            return fn(string)
        except ValueError:
            pass
    return string

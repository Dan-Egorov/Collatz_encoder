def decode(mas: list, key: int, mov: int, nm: float) -> int:
    """
    Function for decoding
    How to work:
    1) fing power of 2
    2) Do the reverse move
    3) Divide numer by nm and get original number
    :param mas: array with number's code
    :param key: power of 2
    :param mov: key for moving power of 2
    :param nm: number for subtract
    :return: original number
    """
    num = 2**(key-mov)
    for i in range(len(mas)-1, -1, -1):
        if mas[i] == 1:
            num *= 2
        elif mas[i] == 0:
            num -= 1
            num //= 3
    if num % nm != 0:
        num //= nm
        num += 1
    else:
        num //= nm
    return num
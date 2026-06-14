def coder(num: int, mov: int, multer: float) -> tuple:
    """
    Function for coding
    How to work:
    1) if num is even, divided by 2 and write in code 1
    2) if num is odd, subtracted by 3 and add 1, write in code 0
    3) if fond the power of 2, stop algorithm
    :param num: number which will coded
    :param mov: number's moving for power
    :param multer: number for mult num
    :return: tuple with power of 2 and code for number
    """
    num = int(num*multer)
    mas = []
    k = 0
    while bin(num)[2:].count("1") != 1:
        if num % 2 == 0:
            num //= 2
            mas.append(1)
        elif num % 2 != 0:
            num *= 3
            num += 1
            mas.append(0)
        if bin(num)[2:].count("1") == 1:
            k = len(bin(num)[2:])-1
            break
    return k+mov, mas
def coder(num: int, mov: int, multer: float) -> tuple:
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
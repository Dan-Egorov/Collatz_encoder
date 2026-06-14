def decode(mas: list, key: int, mov: int, nm: float) -> int:
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
def toThePower(number, power):
    current = number
    for i in range(power - 1):
        current = current * number
    return current

def spiralize(size, n=1):
    x = n
    counter = 0
    incrt = 2
    total = 0

    while x <= size ** 2 + n:
        total += x
        x += incrt
        counter += 1
        if counter == 4:
            incrt += 2
            counter = 0
    return_value = total
    return return_value

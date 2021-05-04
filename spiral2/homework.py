def spiralize(size, n=1):
    x = 1
    counter = 0
    incrt = 2
    return_value = 0

    while x <= size ** 2:
        n += x
        x += incrt
        counter += 1
        if counter == 4:
            incrt += 2
            counter = 0

    return_value = n
    return return_value

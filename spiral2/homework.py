def spiralize(size, n=1):
    spiral = [[1]*size for _ in xrange(size)]
    def ok(y, x):
        return y < size and x < size and y >= 0 and x >= 0 and spiral[y][x]
    y, x, dy, dx = 1, -1, 0, 1
    while ok(y + dy, x + dx):
        if ok(y + 2*dy, x + 2*dx):
            y += dy
            x += dx
        else:
            dx, dy = dy*(2*dx-1), dx
        spiral[y][x] = 0
    return spiral
    return_value = n
    return return_value

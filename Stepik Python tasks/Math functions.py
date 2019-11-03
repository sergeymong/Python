def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif x > 2:
        return (x - 2) ** 2 + 1
    else:
        return -1 * x / 2

def number_pyramid():
    i = 1
    while i <= 5:
        if i % 2 != 0:
            print(" " * (5 - i) + str(i) * (2 * i - 1))
        i += 1

number_pyramid()
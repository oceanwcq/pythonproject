def multiplication_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("{0} * {1} = {2}".format(col, row, col*row), end="\t") # \t help vertical align
            col += 1
        print("") # add a line break between rows
        row += 1
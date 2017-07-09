def multiply(row, col):
    buffer = ''

    for i in range(row):
        for j in range(col):
            buffer = buffer + '  ' + str(j*i) + '  '
        print buffer
        buffer += "\n"
    return buffer
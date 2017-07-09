fila = 10
columna = 10

buffer = ''

for i in range(fila):
    for j in range(columna):
        buffer = buffer + '  ' + str(j*i) + '  '
    print buffer
    buffer = ''

print "\n"
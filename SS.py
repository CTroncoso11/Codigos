salida = []
with open('Base.txt', 'r') as f:
    lineas = [linea.split() for linea in f]

for linea in lineas:
    print(linea)

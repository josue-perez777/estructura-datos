def dividir(a, b, contador=0):
    if a < b:
        return contador
    return dividir(a - b, b, contador + 1)
resultado = dividir(32, 12)
print(resultado)
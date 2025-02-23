def suma_recursiva(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 0:
        return 0
    return arr[n-1] + suma_recursiva(arr, n-1)
arr = [2, 8, 16, 24, 15]
resultado = suma_recursiva(arr)
print(resultado)
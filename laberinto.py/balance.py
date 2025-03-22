def verificar_balance(expresion):
    pila = []
    pares = {'(': ')', '{': '}', '[': ']'}
    errores = []
    
    for i, char in enumerate(expresion):
        if char in pares:  
            pila.append((char, i))  
        elif char in pares.values():  
            if pila and pares[pila[-1][0]] == char:
                pila.pop()  
            else:
                esperado = pares.get(pila[-1][0], 'ninguno') if pila else 'ninguno'
                errores.append(f"Error: '{char}' en posición {i+1}, se esperaba '{esperado}'")
    
    while pila:
        char, pos = pila.pop()
        errores.append(f"Error: '{char}' en posición {pos+1}, falta su cierre '{pares[char]}'")

    return "\n".join(errores) if errores else "Expresión balanceada."

expresiones = [
    "{[()]}",
    "{[(])}",
    "([)]",
    "{[a + b] * (c / d)}",
    "[ ( x + y ) * { 2 + 3 }",
    "({[)]}"
]

for exp in expresiones:
    print(f"Expresión: {exp}")
    print(verificar_balance(exp))
    print("-" * 50)
 
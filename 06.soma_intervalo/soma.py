def soma_intervalo(a, b):
    soma = 0
    if a <= b:
        for i in range(a, b + 1):
            soma += i

    return soma

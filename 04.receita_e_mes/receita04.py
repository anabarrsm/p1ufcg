lucros = []
receitas = []
despesas = []
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for i in range(12):
    valores = input().split()
    receita = float(valores[0])
    despesa = float(valores[1])

    receitas.append(receita)
    despesas.append(despesa)

for v in range(12):
    lucro = receitas[v] - despesas[v]
    lucros.append(lucro)

    if lucro >= 0:
        print(f"{meses[v]}  {lucros[v]:.1f}")

    else:
        print(f"{meses[v]} {lucros[v]:.1f}")

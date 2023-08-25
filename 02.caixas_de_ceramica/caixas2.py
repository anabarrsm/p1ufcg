rev = float(input("Capacidade de revestimento? "))

print("\n== Dados do vão a revestir ==")

comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

area_paredes = (largura * altura) * 4
area_chao = comprimento * largura
area_total = area_paredes + area_chao

caixas = area_total / rev

print(f"\n== Resultados ==\nÁrea total a revestir: {area_total:.1f} m2")
print(f"Número de caixas: {caixas:.0f}")

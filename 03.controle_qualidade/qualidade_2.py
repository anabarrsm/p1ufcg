peso1 = float(input())
peso2 = float(input())

peso_final = (peso1 - peso2) * 100 / peso1

if peso_final < 5:
    print(f"{peso_final:.1f}% do peso do produto é de água congelada.")
    print("Produto qualis A.")

elif peso_final < 10:
    print(f"{peso_final:.1f}% do peso do produto é de água congelada.")
    print("Produto em conformidade.")

else:
    print(f"{peso_final:.1f}% do peso do produto é de água congelada.")
    print("Produto não conforme.")

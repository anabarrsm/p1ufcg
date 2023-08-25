import math

print("Cálculo da Superfície de um Cilindro\n---")
diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

raio = diametro / 2
area_base = math.pi * raio ** 2
area_lateral = 2 * math.pi * raio * altura
area_t = 2 * area_base + area_lateral

print(f"---\nÁrea calculada: {area_t:.2f}")

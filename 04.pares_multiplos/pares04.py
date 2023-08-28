seq = input().split()
cont = 0
pares = []

for i in range(len(seq) - 1):
    num1 = int(seq[i])
    num2 = int(seq[i+1])
    if num1 % num2 == 0 or num2 % num1 == 0:
        cont += 1
        pares.append((num1, num2)) 

print(f"{cont} par(es)")
for n in pares:
    print(n[0], n[1])

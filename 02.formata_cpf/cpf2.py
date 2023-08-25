cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

digitos1 = cpf1 // 100
digitos2 = cpf2 // 100
digitos3 = cpf3 // 100

digitos_final1 = cpf1 % 100
digitos_final2 = cpf2 % 100
digitos_final3 = cpf3 % 100

soma1 = digitos_final1 // 10 + digitos_final1 % 10
soma2 = digitos_final2 // 10 + digitos_final2 % 10
soma3 = digitos_final3 // 10 + digitos_final3 % 10

print(f"{digitos1}-{digitos_final1}\n{soma1}")
print(f"{digitos1}-{digitos_final1}\n{soma2}")
print(f"{digitos1}-{digitos_final1}\n{soma3}")

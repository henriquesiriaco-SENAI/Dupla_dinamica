import os
os.system("Cls")

vetor_numero = []
QUANTIDADE_NUMERO = 10
maioral = 0

for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite o seu {i + 1}° número: "))
    if numero > 10:
        maioral += 1
    vetor_numero.append(numero)

soma = sum(vetor_numero)

print()
print("==== EXIBINDO VALORES ====")
print(f"Soma {soma}")
print(f"Maiores que o número 10: {maioral}")
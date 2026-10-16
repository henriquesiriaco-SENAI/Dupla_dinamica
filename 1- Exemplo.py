import os
os.system("cls")

print("Feito por : Henrique SIRIACO")
print("R.A.: 2020207")

vetor_numero = []
QUANTIDADE_NUMERICAS = 5

for i in range(QUANTIDADE_NUMERICAS):
    numero = int(input(f"Digite {i + 1} Número: "))
    vetor_numero.append(numero)


for i, numero in enumerate(vetor_numero ,start=1):
    print(f" {i}°: {numero}")

print()

for i in  reversed(vetor_numero):
    print(f"{i - 1}°:{numero}")

print("===== FIM =====")
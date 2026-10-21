import os
os.system("cls")

print("Feito por: Henrique")
print("R.A: 20+20+20+7")

vetor_numero = []
QUANTIDADE_NUMERO = 5

for i in range(QUANTIDADE_NUMERO):
    numero = int(input(f"Digite seu {i + 1}° número: "))
    vetor_numero.append(numero)

for numerozinho, numero in enumerate (vetor_numero,start=1): #forEach
    print(f"{numerozinho}°: {numero}")

print()

for  i, numero in enumerate(reversed(vetor_numero )):
    print(f"{i - 1}°: {numero} ")
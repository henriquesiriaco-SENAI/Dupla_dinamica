import os
os.system('cls')


print("Digite os 10 números inteiros")
vetor_A = []
for i in range(10):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor_A.append(valor)

vetor_positivos = []
for numero in vetor_A:
    if numero > 0:
        vetor_positivos.append(numero)



print(f"Vetor_A: {vetor_A}")
print(f"Vetor de positivos: {vetor_positivos}")
print(f"Total de elementos positivos copiados: {len(vetor_positivos)}")
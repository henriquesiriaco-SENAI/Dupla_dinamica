import os
os.system('cls')


print(" Digite os 5 valores do Vetor A:")
vetor_A = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º elemento de A: "))
    vetor_A.append(valor)

print("\n Digite os 5 valores do Vetor B:")
vetor_B = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º elemento de B: "))
    vetor_B.append(valor)

vetor_C = []
for i in range(5):
    vetor_C.append(vetor_A[i] + vetor_B[i])

print(f"Vetor A: {vetor_A}")
print(f"Vetor B: {vetor_B}")
print(f"Vetor C: {vetor_C}")
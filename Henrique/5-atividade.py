import os
os.system("Cls")

vetor_nota = []
QUANTIDADE_NOTAS = 5
acima = 0


for i in range(QUANTIDADE_NOTAS):
    nota = int(input(f"Digite a sua {i + 1}°: "))
    vetor_nota.append(nota)
    if nota >= 7:
        acima += 1

soma = sum(vetor_nota)
media = soma / QUANTIDADE_NOTAS

for notasboas, notas in enumerate (vetor_nota,start=1): #forEach
    print(f"{notasboas}°nota : {notas}")
print(f"Quantidade de pessoas acima da media SETE: {acima}")
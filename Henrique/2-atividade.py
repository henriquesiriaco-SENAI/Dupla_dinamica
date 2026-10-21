import os
os.system("cls")

print("Feito por: Henrique")
print("R.A: 20+20+20+7")

vetor_temp = []
QUANTIDADE_NUMERICA = 7


for i in range(QUANTIDADE_NUMERICA):
    temperatura = int(input(f"Temperatura no {i + 1}° da semana: "))
    vetor_temp.append(temperatura)

maior = max(vetor_temp)
menor = min(vetor_temp)
media = sum(vetor_temp) / QUANTIDADE_NUMERICA
print()
print("=== EXIBINDO DADOS ===")

print(f"Média climatica {media}")
print(f"Maior temperatura {maior}")
print(f"Menor temperatura {menor}")
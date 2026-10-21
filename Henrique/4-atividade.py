import os
os.system("cls")

vetor = []
QUANTIDADE = 8

for i in range(QUANTIDADE):
    numero = int(input(f"Digite o {i + 1 }° número: "))
    vetor.append(numero)

pesquisa = int(input("\n Digite um número para pesquisar: "))

if pesquisa in vetor:
    posicao = vetor.index(pesquisa)
    print(f"o numero {pesquisa} foi encontrado na posição {posicao}.")
else:
    print("Número não encontrado.")
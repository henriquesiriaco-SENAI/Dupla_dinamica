import os
os.system('cls')

nomes = []
salarios = []



print(" Cadastro de Funcionários: ")
for i in range(5):
    print(f" Funcionário {i+1}:")
    nome = input("digite seu nome: ")
    salario = float(input("Salário (R$): "))
    nomes.append(nome)
    salarios.append(salario)


maior_salario = salarios[0]
posicao = 0
acima_2000 = 0

for i in range(5):

    if salarios[i] > maior_salario:
        maior_salario = salarios[i]
        posicao = i
        
    # Conta quantos ganham acima de R$ 2.000,00
    if salarios[i] > 2000:
        acima_2000 += 1

nome_maior_salario = nomes[posicao]


print()
print(f"Maior salário: {nome_maior_salario} (R$ {maior_salario:.2f})")
print(f"Funcionários com salário acima de R$ 2.000,00: {acima_2000}")
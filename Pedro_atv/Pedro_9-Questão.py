import os
os.system('cls')


# Leitura dos 6 números inteiros
print("--- Digite os 6 números inteiros ---")
vetor_A = []
for i in range(6):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor_A.append(valor)

# Criamos uma cópia do vetor original para mostrar "antes" e "depois"
vetor_B = list(vetor_A)

# Substituição: par vira 0, ímpar vira 1
for i in range(len(vetor_A)):
 
    if vetor_A [i] % 2 == 0:
        vetor_B [i]= 0
    else:                  
        vetor_B [i]= 1


print(f"Vetor impar:   {vetor_A}")
print(f"Vetor par:  {vetor_B}")
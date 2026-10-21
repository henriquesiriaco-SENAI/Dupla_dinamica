import os
os.system('cls')

temperaturas = [25,28,30,26,24,27,29]

for dia in range(1,8):
    tempo = float(input(f'digite a temperatura do dia {dia}:'))
    temperaturas.append(tempo)

    media = sum(temperaturas) / len(temperaturas)
    maior = max(temperaturas)
    menor = min(temperaturas)

    print(f'media ,{media}')
    print(f'maior , {maior}')
    print(f'menor , {menor}')

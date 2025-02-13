"""📌 Enunciado:
Crie um jogo onde o computador escolhe um número aleatório de 1 a 100, e o usuário deve adivinhar. O programa deve dar dicas:

"Muito alto!" se o palpite for maior
"Muito baixo!" se o palpite for menor
Informar o número de tentativas ao acertar"""

import random

n_secreto = random.randint(1,100)

tentativas = 0

print("____Jogo da adivinhação____")
print("advinhe o numero entre 1 e 100")

while True:
    try:
        paplpite = int(input("Digite um numero entre 1 e 100:"))
        tentativas += 1

        if paplpite <1 or paplpite >100:
            print("Digite um numero entre 1 e 100:")
            continue
        
        
        
        if paplpite > n_secreto:
            print("palpite muito alto")
        elif paplpite < n_secreto:
            print("palpite muito baixo")
        else:
            print("resposta certa, você acertou em:",tentativas,"tentativas")
    
    except ValueError:
        print("inválido! Digite um número inteiro.")




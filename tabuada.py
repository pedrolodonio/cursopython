"""Tabuada Personalizada (laço while)
📌 Enunciado:
Peça ao usuário um número e gere sua tabuada de multiplicação até que ele digite um número negativo para sair.

💡 Dica: Use while para continuar rodando até o usuário encerrar."""

while True:
    
    num = int(input("Digite um número para descobrir a tabuada (negativo para sair): "))

    
    if num < 0:
        print("encerrando...")
        break

    print(f"\nTabuada do {num}:")
    for i in range(1, 11):  # Multiplica de 1 a 10
        print(f"{num} x {i} = {num * i}")
    
    print()
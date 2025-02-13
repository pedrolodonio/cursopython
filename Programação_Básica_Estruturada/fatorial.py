def fatorial (n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
while True:
    
    num = int(input("Digite um número para descobrir o seu fatorial (negativo para sair): "))

    
    if num < 0:
        print("encerrando...")
        break

    print(fatorial(num))

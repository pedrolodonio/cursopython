"""📌 Descrição: Desenvolva uma calculadora que realiza adição, subtração, multiplicação e divisão, usando uma função para cada operação."""

def soma (a,b): return a+b
def subtracao (a,b): return a-b
def multiplicacao (a,b): return a*b
def divisao (a,b): return a/b

while True:

    print("\n-----Calculadora-----\n")

    print("1-Adição")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão")
    print("5-Exibir todas as operações")
    print("6-Sair")

    opcao = int(input("Selecione uma opção:"))

    if opcao == 6:
        print("encerrando")
        break
    
    elif opcao == 1:
        n = float (input("digite o primeiro número:"))
        n2 = float (input("digite o segundo número:"))
        
        print(f"{n} + {n2} = {soma(n,n2)}")

    elif opcao == 2:
        n = float (input("digite o primeiro número:"))
        n2 = float (input("digite o segundo número:"))
        
        print(f"{n} - {n2} = {subtracao(n,n2)}")

    elif opcao == 3:
        n = float (input("digite o primeiro número:"))
        n2 = float (input("digite o segundo número:"))
        
        print(f"{n} x {n2} = {multiplicacao(n,n2)}")

    elif opcao == 4:
        n = float (input("digite o primeiro número:"))
        n2 = float (input("digite o segundo número:"))
        
        print(f"{n} / {n2} = {divisao(n,n2)}")

    elif opcao == 5:
        n = float (input("digite o primeiro número:"))
        n2 = float (input("digite o segundo número:"))
        
        print(f"{n} + {n2} = {soma(n,n2)}")
        print(f"{n} - {n2} = {subtracao(n,n2)}")
        print(f"{n} x {n2} = {multiplicacao(n,n2)}")
        print(f"{n} / {n2} = {divisao(n,n2)}")
    
    else:
        print("opção inexistente!")

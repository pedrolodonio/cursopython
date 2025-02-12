"""Descrição: Escreva um programa que converta temperaturas entre Celsius e Fahrenheit. O usuário escolhe a conversão desejada.

💡 Dica: Use a fórmula:

Fahrenheit → Celsius: C = (F - 32) * 5/9
Celsius → Fahrenheit: F = (C * 9/5) + 32"""

def temperatura_Celsius (temperaturaF):
    temperaturaC = (temperaturaF-32) * 5/9
    return temperaturaC

def temperatura_Farenheit (temperaturaC):
    temperaturaF = (temperaturaC * 9/5 ) + 32
    return temperaturaF

while True:

    print("\nSelecione uma opção:")
    print("1 - Converter temperatura Celsius para Farenheit")
    print("2 - Converter temperatura Farenheit para Celsius")
    print("3 - Sair")
    
    
    opcao = int(input("Digite a opção desejada: "))
    

    if opcao == 3:
        print("encerrando")
        break
    elif opcao == 1 :
        temperaturaC = float(input("Digite a temperatura em Celsius:"))
        temperaturaF = temperatura_Farenheit(temperaturaC)
        print("a temperatura "+ str(temperaturaC) +"C° é equivalente a " + str(temperaturaF)+"F°")
    elif opcao == 2 :
        temperaturaF = float(input("Digite a temperatura em Farenheit:"))
        temperaturaC = temperatura_Celsius(temperaturaF)
        print("a temperatura "+ str(temperaturaF) +"F° é equivalente a " + str(temperaturaC) +"C°")
    else:
        print("Opção inválida! Digite um número entre 1 e 3.")

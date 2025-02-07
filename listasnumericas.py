"""📌 Enunciado:
Peça ao usuário para inserir 10 números e armazene em uma lista. Em seguida, exiba:

A lista ordenada de forma crescente
A soma dos valores
A quantidade de números pares"""

elementos = (input("digite numeros inteiros separados por virgula: "))
numeros = list(map(int,elementos.split(",")))

print(numeros)
soma_numeros = sum(numeros)
print(soma_numeros)
i = 0
for numero in numeros:
    if numero%2 == 0:
        i += 1

print("a quantidade de numeros pares é ",i)
    



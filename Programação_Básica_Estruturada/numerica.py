"""📌 Enunciado:
Crie um programa que peça três números ao usuário e exiba:

A média aritmética
O maior e o menor número
A diferença entre o maior e o menor"""

n1 = float(input("digite um numero:"))
n2 = float(input("digite um numero:"))
n3 = float(input("digite um numero:"))

lista = [n1,n2,n3]

media = (n1+n2+n3)/3
print("a média é:",media)
print("o maior numero é:",max(lista))
print("o menor numero é:",min(lista))
print(max(lista),"-",min(lista),"=",max(lista)-min(lista))






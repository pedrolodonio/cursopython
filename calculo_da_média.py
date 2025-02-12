"""Descrição: Crie um programa que solicite ao usuário três notas de um aluno e calcule a média. O programa deve imprimir a média e informar se o aluno está aprovado (média >= 7) ou reprovado.
Dicas:
Use variáveis para armazenar as notas.
Utilize uma estrutura condicional para determinar a situação do aluno.
"""
from statistics import mean as media

notas = input("Digite exatamente 3 notas separadas por espaço: ").split()
if len(notas) == 3:
    try:
        notas = [float(nota) for nota in notas]  # Converte para float
    except ValueError:
        print("Erro! Certifique-se de digitar apenas números.")
else:
    print("Você deve inserir exatamente 3 notas!")

media_notas = media(notas)

print(media_notas)

if media_notas >=7:
    print ("Aluno Aprovado")
else:
    print ("Aluno Reprovado")
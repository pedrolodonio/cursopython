"""📌 Enunciado:
Crie uma tupla com nomes de 5 produtos e outra com os respectivos preços. Depois, exiba uma tabela formatada"""

produtos =("Fearless","1989","folklore","Midnights","The Tortured Poets Department")
preços = (13.99,19.89,20.20,20.22,20.24)

print(f"{'Produto':<10}{'Preço':>5}") 
print("-" * 16)
for produto,preço in zip(produtos,preços):
    print (f"{produto:<10} R${preço:.2f} ")

"""Crie uma classe chamada Carro, que tenha os atributos marca, modelo e ano. Depois, instancie dois objetos dessa classe e exiba seus atributos.

📌 Dicas:

Use o método __init__() para inicializar os atributos.
Crie objetos da classe e exiba as informações de cada um"""

class Carro:
    
    def __init__ (self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro_1 = Carro("Toyota","Corolla","2026")
carro_2 = Carro("Renault","Kwid","2020")

print(f"{carro_1.marca}  {carro_1.modelo}  {carro_1.ano}")
print(f"{carro_2.marca}  {carro_2.modelo}  {carro_2.ano}")



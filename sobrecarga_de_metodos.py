""" Sobrecarga de Métodos (__init__)
Crie uma classe Produto que tenha dois tipos de inicialização:

Se for passado apenas nome e preço, a categoria será "Diversos".
Se for passado também a categoria, deve armazená-la corretamente.
📌 Dicas:

Use valores padrão no __init__() para simular sobrecarga.
Teste criando produtos com e sem a categoria."""

class Produto:
    def __init__(self,nome,preco, categoria="Diversos"):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

produto1 = Produto ("Lapiseira","R$ 13.00")
produto2 = Produto ("Borracha","R$ 7.00","papelaria")

print(f"{produto1.nome}  {produto1.preco}  {produto1.categoria}")
print(f"{produto2.nome}  {produto2.preco}  {produto2.categoria}")

        
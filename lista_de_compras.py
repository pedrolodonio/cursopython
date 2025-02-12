"""Gerenciador de Lista de Compras 🛒
📌 Descrição: Implemente um sistema onde o usuário pode:

Adicionar itens a uma lista de compras.
Remover itens da lista.
Listar todos os itens.
Sair do programa."""

lista_de_compras = []

while True:

    print("\nLista de Compras\n")
    print("1-Adicionar itens a lista")
    print("2-Remover itens da lista")
    print("3-Listar todos os itens")
    print("4-Sair")
    
    opcao = int(input("Selecione uma opção:"))

    if opcao == 4:
        print("Encerrando aplicação...")
        break
    
    elif opcao == 1:
        produto = str.lower(input("Digite o produto que deseja inserir:"))
        lista_de_compras.append(produto)
        print(f"{produto} adicionado a sua lista de compras")
    
    elif opcao == 2:
        produto = str.lower(input("Digite o produto que deseja remover:"))
       
        if produto in lista_de_compras:
            lista_de_compras.remove(produto)
            print(f"{produto} foi removido da sua lista de compras")
        else:
            print("produto não encontrado")
    
    elif opcao == 3:
        print("\nLista de compras\n")
        for i , produto in enumerate(lista_de_compras,1):
            print(f"{i}-{produto}")
    
    else:
        print("opção inválida")



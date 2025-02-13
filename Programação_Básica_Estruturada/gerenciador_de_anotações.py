"""Crie um programa que permita ao usuário gerenciar um arquivo de notas.txt. O programa deve oferecer as seguintes opções:
1️⃣ Adicionar uma nova nota ao arquivo.
2️⃣ Ler todas as notas do arquivo.
3️⃣ Buscar notas por palavra-chave.
4️⃣ Excluir todas as notas.
5️⃣ Sair do programa."""

def adicionar_anotacao():
    with open ("anotações.txt","a") as arquivo:
        anotacao = input("digite sua anotação:")
        arquivo.write(anotacao + "\n")
    print("anotação feita com sucesso")

def ler_anotacao():
    with open("anotações.txt","r") as arquivo:
        anotacoes = arquivo.readlines()
        if anotacoes:
            print("anotações registradas:\n")
            for i,anotacao in enumerate(anotacoes,1):
                print(f"{i}-{anotacao.strip()}")
        else:
            print("nenhuma anotação registrada")

def key_word():
    palavra_chave = input("digite a palavra chave:")

    try:
        with open("anotações.txt","r") as arquivo:
            anotacoes = arquivo.readlines()
            encontradas = [anotacao for anotacao in anotacoes if palavra_chave.lower() in anotacao.lower()]

            if encontradas:
                print("notas encontradas:")
                for i, anotacao in enumerate(encontradas,1):
                    print(f"{i}-{anotacao.strip()}")
            else:
                print(f"{palavra_chave} não foi encontrada em nenhuma anotação")

    except FileNotFoundError:
        print("nenhuma nota registrada")
    print()

def deletar_tudo():
    with open ("anotações.txt","w") as arquivo:
        pass
    print("anotações deletadas")

while True:
    print("\nBloco de notas\n")
    print("1-Adicionar Nota")
    print("2-Ler todas as Notas")
    print("3-Buscar por palavra chave")
    print("4-Deletar todas as notas")
    print("5-Sair")

    opcao = input("digite a opção desejada:")

    if opcao == '5':
        print("Encerrando...")
        break

    elif opcao == '1':
        adicionar_anotacao()
    elif opcao == '2':
        ler_anotacao()
    elif opcao == '3':
        key_word()
    elif opcao == '4':
        deletar_tudo()
    else:
        print("opção inválida")

    
    








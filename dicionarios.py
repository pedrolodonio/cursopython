"""📌 Enunciado:
Crie um sistema que permita cadastrar usuários e suas informações (nome, idade, email) em um dicionário. O programa deve permitir:

Cadastrar um novo usuário
Listar todos os usuários
Buscar um usuário pelo nome
💡 Dica: Use um dicionário usuarios[nome] = {"idade": idade, "email": email}."""

usuários = []

while True:

    print("\nSelecione uma opção:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Buscar usuários pelo nome")
    print("4 - Sair")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida! Digite um número entre 1 e 4.")
        continue
    
    if opcao == 4:
        print("Encerrando...")
        break
    
    elif opcao == 1:
        nome = input("Digite o nome do usuário:")
        idade = input("Digite a idade do usuário:")
        email = input("Digite o email do usuário:")

        usuário = {"Nome": nome, "Idade": idade, "E-mail":email}
        usuários.append(usuário)
        print(f"{nome} cadastrado com sucesso!")
    
    elif opcao == 2:
        if not usuários:
            print("nenhum usuário cadastrado")
            continue

        print("\nLista de Usuários")
       

        for usuário in usuários:
            print(f"Usuário:{usuário['Nome']} - Idade:{usuário['Idade']} - E-mail:{usuário['E-mail']}")
    
    elif opcao == 3:
        if not usuários:
            print("Nenhum usuário foi cadastrado")
            continue

        busca_nome = input("Digite o nome do usuário:")
        encontrado = False

        for usuário in usuários:
             if usuário["Nome"].lower() == busca_nome.lower():
                print(f"Usuário Encontrado\nNome:{usuário['Nome']} - Idade:{usuário['Idade']} - E-mail:{usuário['E-mail']}")
                encontrado = True
                break
             if not encontrado:
                 print("usuário inexistente")



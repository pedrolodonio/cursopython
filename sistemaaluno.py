"""📌 Enunciado:
Crie um dicionário onde as chaves são nomes de alunos e os valores são listas com 3 notas. O programa deve permitir:

Cadastrar novos alunos
Exibir a média de um aluno específico
Exibir todos os alunos com média maior ou igual a 7.0"""

alunos = []

while True:
   
    print("\nSelecione uma opção:")
    print("1 - Cadastrar novo aluno")
    print("2 - Exibir média de um aluno")
    print("3 - Exibir alunos com média acima de 7")
    print("4 - Sair")

    # Entrada do usuário com tratamento de erro
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida! Digite um número entre 1 e 4.")
        continue

    if opcao == 4:
        print("Encerrando...")
        break
    elif opcao == 1:
        nome = input("Digite o nome do aluno: ")

        while True:
            notas = input("Digite exatamente 3 notas separadas por espaço: ").split()
            if len(notas) == 3:
                try:
                    notas = [float(nota) for nota in notas]  # Converte para float
                    break
                except ValueError:
                    print("Erro! Certifique-se de digitar apenas números.")
            else:
                print("Você deve inserir exatamente 3 notas!")

        # Criando o dicionário do aluno e adicionando à lista
        aluno = {"nome": nome, "notas": notas}
        alunos.append(aluno)
        print(f"{nome} cadastrado com sucesso!")
    
    elif opcao == 2:
        if not alunos:
            print("Nenhum aluno cadastrado ainda.")
            continue
        
        busca_nome = input("digite o nome do aluno:") 
        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == busca_nome.lower():
                media = sum(aluno["notas"])/len(aluno["notas"])
                print(f"A média de {aluno['nome']} é {media:.2f}")
                encontrado = True
                break
            
            if not encontrado:
                print("aluno não encontrado")
    elif opcao == 3:
        if not alunos:
            print("nenhum aluno cadastrado")
            continue

        print("\nAlunos com média acima de 7")
        encontrou = False

        for aluno in alunos:
            media = sum(aluno["notas"])/len(aluno["notas"]) 
            if media >= 7:
                print(f"{aluno['nome']} - Média: {media:.2f}")
            encontrou = True

        if not encontrou:
            print("Nenhum aluno com média acima de 7.")

    else:
        print("Opção inválida! Digite um número entre 1 e 4.")





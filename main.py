from funcoes_contatos import adicionar, listar_contatos, favoritar_contato, listar_favoritos, editar_contato, deletar_contato, ordenar_lista, validar_email, validar_telefone


contatos = []

while True:
    print("\nMenu de opções:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Favoritar/Desfavoritar contato")
    print("5. Listar contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair\n")

    escolha = input("\nDigite a sua opção: ")
    
    ordenar_lista(contatos)

    if escolha == "1":
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone do contato (xx)xxxxx-xxxx: ")
        if validar_telefone(telefone) == False:
            print("Formato inválido")
            telefone = ("Inválido")
        email = input("Digite o email do contato: ")
        if validar_email(email) == False:
            print("Formato Inválido")
            email = ("Inválido")
        adicionar(contatos, nome, telefone, email)
    
    elif escolha == "2":
        print("\n--- LISTA COMPLETA DE CONTATOS ---")
        listar_contatos(contatos)

    elif escolha == "3":
        print("\n--- LISTA COMPLETA DE CONTATOS ---")
        listar_contatos(contatos)
        indice = int(input("\nDigite o indice do contato que deseja alterar? "))
        novo_nome = input("Qual o novo nome? ")
        novo_telefone = input("Qual o novo telefone? ")
        novo_email = input("Qual o novo email? ")
        editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email)
        print("\n--- LISTA COMPLETA ATUALIZADA ---")
        listar_contatos(contatos)    

    elif escolha == "4":
        listar_contatos(contatos)
        indice = int(input("\nQual o indice do contato você deseja favoritar ou desfavoritar? "))
        favoritar_contato(contatos, indice)

    elif escolha == "5":
        print("\n--- LISTA COMPLETA DE FAVORITOS ---")
        listar_favoritos(contatos)
        print("\nLista carregada com sucesso!")

    elif escolha == "6":
        listar_contatos(contatos)
        indice = int(input("Qual contato deseja deletar? "))
        deletar_contato(contatos, indice)

    elif escolha == "7":
        print("Saindo do programa...")
        break
import re

def ordenar_lista(contatos):
        contatos.sort(key=lambda contato: (not contato["favorito"], contato["nome"]))
        return contatos

def puxar_lista(contatos):
    for indice, contato in enumerate(contatos, start=1):
        favorito = "⭐" if contato["favorito"] else ""
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        if contato["favorito"] == True:
            print(f"\n{indice}. {favorito} {nome_contato}")
            print(f"Telefone: {telefone_contato}")
            print(f"Email: {email_contato}")
        else:
            print(f"\n{indice}. {nome_contato}")
            print(f"Telefone: {telefone_contato}")
            print(f"Email: {email_contato}")
        
        if validar_email(email_contato) == False and validar_telefone(telefone_contato) == False:
            print("Precisa validar o seu email e telefone!")
        elif validar_email(email_contato) == False:
            print("Precisa validar o email")
        elif validar_telefone(telefone_contato) == False:
            print("Precisa validar seu telefone")
        

def adicionar(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    return

def listar_contatos(contatos):
    puxar_lista(contatos)

def favoritar_contato(contatos, indice):
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado <= len(contatos) and contatos[indice_ajustado]["favorito"] == False:
        contatos[indice_ajustado]["favorito"] = True
        return contatos[indice_ajustado]
    else:
        contatos[indice_ajustado]["favorito"] = False
        return contatos[indice_ajustado]

def listar_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        favorito = "⭐" if contato["favorito"] else ""
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        if contato["favorito"] == True:
            print(f"\n{indice}. {favorito} {nome_contato}")
            print(f"Telefone: {telefone_contato}")
            print(f"Email: {email_contato}")


def editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email):
    indice_ajustado = indice - 1
    contatos[indice_ajustado]["nome"] = novo_nome
    contatos[indice_ajustado]["telefone"] = novo_telefone
    contatos[indice_ajustado]["email"] = novo_email
    print("\n--- LISTA ATUALIZADA ---")
    listar_contatos(contatos)

def deletar_contato(contatos, indice):
    indice_ajustado = indice - 1
    for indice_contato, contato in enumerate(contatos):
        nome_contato = contato["nome"]
    print("\nTem certeza que deseja deletar esse contato? ")
    print("1 - Sim")
    print("2 - Não")
    escolha_texto = input("\nIndice: ")
    if escolha_texto == "1" or escolha_texto == "Sim" or escolha_texto == "sim":
        del contatos[indice_ajustado]
        print(f"Contato {indice_contato}.{nome_contato} deletado com sucesso!")
        return
    else:
        return print("Nenhum contato deletado")

def validar_telefone(telefone):
    padrao_telefone = r"^\(\d{2}\)\d{5}\-\d{4}$"
    if re.match(padrao_telefone, telefone):
        return True
    return False

def validar_email(email):
    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(padrao_email, email):
        return True
    return False
    
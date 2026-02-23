from dao.aluno_dao import AlunoDAO
import time

dao = AlunoDAO()


def menu_inicial():
    print("""
O que você deseja fazer?

1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno por ID
4 - Atualizar aluno
5 - Remover aluno
0 - Sair
""")

    while True:
        try:
            return int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite apenas números.")


def create():
    while True:
        nome = input("Nome: ")

        while True:
            try:
                idade = int(input("Idade: "))
                break
            except ValueError:
                print("Digite apenas números.")

        curso = input("Curso: ")

        dao.create(nome, idade, curso)
        print("Aluno cadastrado com sucesso!")

        continuar = input("Deseja continuar? (y/n): ").lower()
        if continuar != "y":
            break


def read():
    alunos = dao.read()

    if not alunos:
        print("Nenhum aluno encontrado.")
        return

    for aluno in alunos:
        print(f"ID: {aluno.id} | Nome: {aluno.nome} | Idade: {aluno.idade} | Curso: {aluno.curso}")


def search_by_id():
    try:
        id = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return

    aluno = dao.read_by_id(id)

    if aluno:
        print(f"ID: {aluno.id} | Nome: {aluno.nome} | Idade: {aluno.idade} | Curso: {aluno.curso}")
    else:
        print("Aluno não encontrado.")


def update():
    try:
        id = int(input("Digite o ID do aluno: "))
    except ValueError:
        print("ID inválido.")
        return

    aluno = dao.read_by_id(id)

    if not aluno:
        print("Aluno não encontrado.")
        return

    nome = input(f"Novo nome ({aluno.nome}): ") or aluno.nome

    try:
        idade_input = input(f"Nova idade ({aluno.idade}): ")
        idade = int(idade_input) if idade_input else aluno.idade
    except ValueError:
        print("Idade inválida.")
        return

    curso = input(f"Novo curso ({aluno.curso}): ") or aluno.curso

    dao.update(id, nome, idade, curso)
    print("Aluno atualizado com sucesso.")


def remover():
    try:
        id = int(input("Digite o ID do aluno: "))
    except ValueError:
        print("ID inválido.")
        return

    aluno = dao.read_by_id(id)

    if not aluno:
        print("Aluno não encontrado.")
        return

    dao.delete(id)
    print("Aluno removido com sucesso.")


while True:
    opcao = menu_inicial()

    if opcao == 1:
        create()
    elif opcao == 2:
        read()
    elif opcao == 3:
        search_by_id()
    elif opcao == 4:
        update()
    elif opcao == 5:
        remover()
    elif opcao == 0:
        print("Programa finalizado.")
        dao.close()
        break
    else:
        print("Opção inválida.")

    time.sleep(1)
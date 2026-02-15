from aluno import Aluno
import time
def menu_inicial():
    print("""O que você deseja fazer?
          
////////// 1 - Cadastrar aluno: //////////
////////// 2 - Listar alunos: //////////
////////// 3 - Listar alunos por ID: //////////
////////// 4 - Atualizar aluno: //////////
////////// 5 - Remover aluno: //////////
////////// 0 - Sair //////////""")

    while True:
            try:
                opcao=int(input("\nDigite a opção desejada: ")) 
                break
                
            except ValueError:
                print("Opção inválida. Digite apenas números.") 
    return opcao   
            
    
def create():
    opcao = 1
    while opcao == 1:
        nome = input("\nDigite o nome do aluno: ")
        
        while True:
            try:
                idade = int(input("Digite a idade do aluno: "))
                break
            except ValueError:
                print("Idade inválida. Digite apenas números.")
                    
        curso = input("Digite o curso do aluno: ")
        
        if alunos == []:
                id = 1
        else: 
            id = 1
            id_existe = True
            while id_existe:
                id_existe = False
                for aluno in alunos:
                    if aluno.id == id:
                        id += 1
                        id_existe = True
                        break
                
        novo_aluno = Aluno(id, nome,idade,curso)
        alunos.append(novo_aluno)
            
        opcao = input("Deseja continuar adcionando alunos? [y/n]: ").lower()

            
        if  opcao == "y":
                opcao = 1
                    
        elif opcao == "n":
            break
                  
        else:
            print("Opção inválida!")
            print("Você será redirecionado para o menu inicial!")
                
                
                
def read():
    if not alunos:
        print("Não foram encontrados alunos")
        time.sleep(2)
        
    else:
        while True:
            print("""Qual ordem você gostaria de ver?
          
////////// 1 - Listar alunos por data de inclusão no sistema: //////////
////////// 2 - Listar alunos por ID: //////////
////////// 3 - Listar alunos por Idade: //////////
////////// 4 - Listar alunos por Ordem Alfabética: //////////""")
    
            while True:
                    try:
                        opcao=int(input("\nDigite a opção desejada: ")) 
                        break
                        
                    except ValueError:
                        print("Opção inválida. Digite apenas números.")  
            
            if opcao == 1:
                for aluno in alunos:
                    print(f" Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")
                time.sleep(2)
                contiuar_listando = ("Deseja listar alunos novamente utilizando outros critérios? [y/n]")
                
                if contiuar_listando == "y":
                    print("Perfeito! você será redirecionado ao menu de listagem!")
                    time.sleep(2)
        
                
                elif contiuar_listando == "n":
                    break
                
                else:
                    print("Opção inválida! Você será redirecionado para o Menu Inicial!")
                    break

            
            elif opcao == 2:    
                nova_lista = sorted(alunos, key=lambda aluno: aluno.id)
                for aluno in nova_lista:
                    print(f" Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")
                time.sleep(2)
                
                contiuar_listando = ("Deseja listar alunos novamente utilizando outros critérios? [y/n]")
                
                if contiuar_listando == "y":
                    print("Perfeito! você será redirecionado ao menu de listagem!")
                    time.sleep(2)
                
                elif contiuar_listando == "n":
                    break
                
                else:
                    print("Opção inválida! Você será redirecionado para o Menu Inicial!")
                    break
        
            
            elif opcao == 3:
                nova_lista = sorted(alunos, key=lambda aluno: aluno.idade)
                for aluno in nova_lista:
                    print(f" Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")
                time.sleep(2)
                
                contiuar_listando = ("Deseja listar alunos novamente utilizando outros critérios? [y/n]")
                
                if contiuar_listando == "y":
                    print("Perfeito! você será redirecionado ao menu de listagem!")
                    time.sleep(2)
                
                elif contiuar_listando == "n":
                    break
                
                else:
                    print("Opção inválida! Você será redirecionado para o Menu Inicial!")
                    break
        
            elif opcao == 4:
                nova_lista = sorted(alunos, key=lambda aluno: aluno.nome)
                for aluno in nova_lista:
                    print(f" Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")
                time.sleep(2)
                
                contiuar_listando = ("Deseja listar alunos novamente utilizando outros critérios? [y/n]")
                
                if contiuar_listando == "y":
                    print("Perfeito! você será redirecionado ao menu de listagem!")
                    time.sleep(2)
                
                elif contiuar_listando == "n":
                    break
                
                else:
                    print("Opção inválida! Você será redirecionado para o Menu Inicial!")
                    break
            
            
            else: 
                print("Opção inválida!")
                print("Você será redirecionado para o menu inicial!")
                time.sleep(2)
                break
       
        
def search_by_id():
    if alunos == []:
        print("Opção inválida!")
        print("Você será redirecionado para o menu inicial!")
        time.sleep(2)
       
        
    else:       
            while True:
                
                while True: 
                    try:
                        id = int(input("Digite o ID que você quer pesquisar: "))
                        break 
                    
                    except ValueError:
                        print("ID inválido. Digite apenas números.")
                          
                
                achar_id = True    
                
                while achar_id == True: 
                    for aluno in alunos:
                        if id == aluno.id:
                            print(f"Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso} ")
                            achar_id = False
                            break 
    
                    else:
                        print("Não existe nenhum Aluno cadastrado nesse ID!")
                        break
        
                time.sleep(2)
                
                opcao = input("Deseja consultar outro ID? [y/n] ").lower()
                
                if opcao == "y":
                    continue
                    
                elif opcao == "n":
                    print("Você será redirecionado para o menu inicial! ")
                    time.sleep(2)
                    break
                
                else: 
                    print("Opção Inválida! Você será redirecionado para o menu inicial!")
                    time.sleep(2)
                    break

def update():
    if alunos == []:
        print("Opção inválida!")
        print("Você será redirecionado para o menu inicial!")
        time.sleep(2)

    
    else:
        apoio = True
        while apoio == True:
          
          while True:
            try:
                id = int(input("Digite o ID do aluno que você quer alterar: "))
                break
            
            except ValueError:
                print("ID inválido. Digite apenas números.") 
            
          for aluno in alunos:
                if id == aluno.id:
                    print("""\nO que você deseja fazer?

////////// 1 - Alterar nome: //////////
////////// 2 - Alterar idade: //////////
////////// 3 - Alterar curso: //////////""")
                           
                    while True:
                            try:
                                opcao = int(input("\nDigite a opcao você quer alterar: "))
                                break
            
                            except ValueError:
                                print("ID inválido. Digite apenas número")
                            
                    if opcao == 1:
                        novo_nome = input("Digite o novo nome: ")
                        aluno.nome = novo_nome
                        opcao = input("Deseja alterar alterar outra informação? [y/n] ").lower()
                        
                        if opcao == "y":
                            break
                        
                        elif opcao == "n":
                             apoio = False 
                             break
                        
                        else: 
                            print("Opção inválida! Você será redirecionado para o Menu Inicial!") 
                            apoio = False
                            break

                    elif opcao == 2:
                        nova_idade = input("Digite a idade: ")
                        aluno.idade = nova_idade
                        opcao = input("Deseja alterar alterar outra informação? [y/n] ").lower()
                        
                        if opcao == "y":
                            break
                        
                        elif opcao == "n":
                             apoio = False 
                             break
                        
                        else: 
                            print("Opção inválida! Você será redirecionado para o Menu Inicial!") 
                            apoio = False
                            break
                    
                    elif opcao == 3:
                         novo_curso = input("Digite o novo curso: ")
                         aluno.curso = novo_curso 
                         opcao = input("Deseja alterar alterar outra informação? [y/n] ").lower()
                        
                         if opcao == "y":
                             break
                        
                         elif opcao == "n":
                             apoio = False 
                             break
                        
                         else: 
                            print("Opção inválida! Você será redirecionado para o Menu Inicial!") 
                            apoio = False
                            break            
                    
                else:
                      print("Não existe nenhum usuário cadastrado nesse ID!")
                      apoio = False
                      break
                     

def remover():
    if alunos == []:
        print("Opção inválida!")
        print("Você será redirecionado para o menu inicial!")
        time.sleep(2)
    
    else:
        
      while True:
         for aluno in alunos:
            print(f" Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")         
          
          
         while True:
            try:
                id = int(input("Digite o ID do aluno que você quer remover: "))
                break
               
            except ValueError:
                print("ID inválido. Digite apenas números.")
            

         while True:
                for aluno in alunos:
                    if id == aluno.id:
                        alunos.remove(aluno)
                        print(f"O aluno de ID {id} foi removido com sucesso!")
                        for aluno in alunos:
                            print(f" Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")
                        break
                    
                else:
                    print("Não existe nenhum usuário cadastrado nesse ID!")
                    
                break
            
         continuar = input("Deseja continuar removendo alunos? [y/n]: ").lower()
         
         if continuar == "y":
             if alunos == []:
                print("Não existe nenhum aluno cadastrato, é impossível remover alunos!")
                time.sleep(2)
                print("Você será redirecionado para o Menu Inicial!")
                time.sleep(2)
                break
             else: 
                continue
             
         
         elif continuar == "n":
             time.sleep(1)
             break
         
         else:
            print("Opção inválida! Você será redirecionado para o Menu Inicial!")
            time.sleep(1)
            break
        
    
        
            

        
alunos = []  

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
        print("Programa finalizado")
        break
    
    else:
        print("Opção inválida")




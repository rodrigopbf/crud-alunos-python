from dao.aluno_dao import AlunoDAO
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
        
        dao.create(nome,idade,curso)
         
        print("Aluno cadastrado com sucesso!")
        time.sleep(1)   
        opcao = input("Deseja continuar adcionando alunos? [y/n]: ").lower()

            
        if  opcao == "y":
                opcao = 1
                    
        elif opcao == "n":
            break
                  
        else:
            print("Opção inválida!")
            print("Você será redirecionado para o menu inicial!")
                
                

def read():
    alunos = dao.read()
    
    if not alunos:
        print("Não foram encontrados alunos! ")
        time.sleep(2)
        
    else:
        while True:
            print("""Qual ordem você gostaria de ver?
          
////////// 1 - Listar alunos por data de inclusão no sistema: //////////
////////// 2 - Listar alunos por ID: //////////
////////// 3 - Listar alunos por Idade: //////////
////////// 4 - Listar alunos por Ordem Alfabética: //////////
////////// 0 - Sair do Menu de Listagem: //////////""")
    
            while True:
                    try:
                        opcao=int(input("\nDigite a opção desejada: ")) 
                        break
                        
                    except ValueError:
                        print("Opção inválida. Digite apenas números.")  
            
            opcoes = {
                1: alunos,
                2: sorted(alunos, key = lambda aluno:aluno.id),
                3: sorted(alunos, key = lambda aluno:aluno.idade),
                4: sorted(alunos, key = lambda aluno:aluno.nome)
            }
        
            if opcao not in opcoes:
                print("Opção Inválida! Você seráa redirecionado para o Menu Inicial!")
                time.sleep(2)
                break
            
            elif opcao == 0:
                time.sleep(0.5)
                break
            
            else:
                continuar = listar_nova_lista_e_perguntar(opcoes[opcao])
                if not continuar:
                    break
                
def listar_nova_lista_e_perguntar(nova_lista):
                for aluno in nova_lista:
                    print(f" Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")
                
                continuar_listando = input("Deseja listar alunos novamente usando outros critérios? [y/n] ").lower() 
                
                if continuar_listando == "y":
                    print("Perfeito! Você será redirecionado para o Menu de Listagem!")
                    time.sleep(2)
                    return True
                
                elif continuar_listando == "n":
                    return False
                
                else:
                    print("Opção inválida! Você será redirecionado para o Menu Inicial!")
                    return False    
              
                
def search_by_id():
 while True:
    while True:
        try:
            id = int(input("Digite o ID: "))
            break
        except ValueError:
            print ("ID inválido")
            time.sleep(0.5)
           
        
    aluno = dao.read_by_id(id)
        
    if aluno:
        print(f"Id: {aluno.id} - Nome: {aluno.nome} - Idade: {aluno.idade} - Curso: {aluno.curso}")
            
    else:
        print("Aluno não encontrado")

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
    while True:
        try: 
            id = int(input("Digite o ID do aluno: "))
            break
        except ValueError:
            print("ID inválido! ") 
            time.sleep(1) 
       
    aluno = dao.read_by_id(id)
    
    if not aluno:
        print("Não existe nenhum aluno com esse ID ainda! Você precisar adcionar um aluno com esse ID para atualizar!")
        time.sleep(2)
        
    else: 
        nome = aluno.nome
        idade = aluno.idade
        curso = aluno.curso
        
        while True:
            print("""\nO que você deseja alterar?

////////// 1 - Alterar nome: //////////
////////// 2 - Alterar idade: //////////
////////// 3 - Alterar curso: //////////
////////// 0 - Sair do Menu de Alterações: //////////""")
                           
            while True:
                try:
                    opcao = int(input("\nDigite a opcao que você quer alterar: "))
                    break
                
                except ValueError:
                    print("ID inválido. Digite apenas número")
                                
            if opcao == 1:
                nome = input("Digite o novo nome: ")

            elif opcao == 2:
                while True:    
                    try:
                        idade=int(input("Digite a nova idade: "))
                        break
                    except ValueError:
                        print("Idade inválida! Digite apenas números")
                        time.sleep(1) 
                    
            elif opcao == 3:
                curso = input("Digite o novo curso: ") 
                
            elif opcao == 0:
                time.sleep(0.5)
                break
                        
            else:
                    print("Opção Inválida! Tente Novamente!")
                    return
                        
            dao.update(id,nome,idade,curso)
            print("Aluno atualizado com sucesso!")
            time.sleep(2)    
                
            opcao = input("Deseja alterar outra informação? [y/n] ").lower()
            if opcao != "y":
             break      

def remover():
   while True: 
    while True:
        try:
            id = int(input("Digite o ID do aluno: "))
            break
        except ValueError:
            print("ID inválido!")
            time.sleep(2)
            
    aluno = dao.read_by_id(id)
        
    if not aluno:
        print("Aluno não encontrado!")
        time.sleep(2)
        
            
    else:
        dao.delete(id)
        print("Aluno removido com sucesso!")
        time.sleep(2)
    
    continuar = input("Deseja continuar deletando alunos? [y/n] ").lower()
    
    if continuar == "y":
        continue
    
    elif continuar == "n":
        time.sleep(0.5)
        break
    else:
        print("Opção inválida! Você será redirecionado para o Menu Inicial!")
        break
        

dao = AlunoDAO()        

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


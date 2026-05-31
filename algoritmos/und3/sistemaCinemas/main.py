import os
lista_usuarios = []

def usuarios():
      global lista_usuarios
      
      chave = 'S'
      print("""
            Menu

            0 - Cadastrar Usuários
            1 - Listar Usuários
            2 - Excluir Usuário
            3 - Editar Usuáro
            4 - Voltar
                  
                  """)
      opcao = int(input('Digite sua ação: '))
      if opcao == 0:
            nome = input('Digite o nome do usuario: ')
            cpf = input('Digite o cpf do usuario : ')
            email = input('Digite um email do usuário: ')
            senha = input('Digite uma senha : ')
            usuario = [nome,cpf,email,senha]
            lista_usuarios.append(usuario)
            return print('\nUsuário cadastrado com sucesso!\n')
      elif opcao == 1 :
            print(
            """
      Lista de usuários
            """)
            print("_"*60)
            print()
            for usuario in lista_usuarios:
                  print(f'''
      Nome : {usuario[0]}
      Email : {usuario[2]}
                        ''')
      
      elif opcao == 2:
            nome = input('Digite o nome do usuário que deseja excluir: ')
            if nome in lista_usuarios:
                  for usuario in lista_usuarios:
                        if nome==usuario[0]:
                              lista_usuarios.remove(usuario)
            else:
                  print('Usuário não encontrado!')
            
            
            
      
            
      

chave = 'S'


while chave=='S':
     
      print("_"*60)
      print(
            """
            MovieSync - Sistema de Gestão de Cinemas
            """)
      print("_"*60)
    
      print("""
Menu

0 - Módulo de Usuários
1 - Módulo de Filmes
2 - Módulo de Ingressos
3 - Módulo de Relatórios
4 - Sobre o Sistema
5 - Sair
          
          """)
      opcao = int(input('Escolha o módulo que deseja acessar. [0-8] :'))
      print()

      if opcao == 5:
            chave = 'N'
            print()
            input("Tecle <ENTER> para continuar...")
      
      elif opcao == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
            """
      Módulo de Usuários
            """)
            print("_"*60)
            
            usuarios()
            
      
      elif opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
            Módulo de Filmes
                  """)
            print("_"*60)
            print("""
            Este módulo ainda está
            em desenvolvimento 
                  
                  """)
            print()
            input("Tecle <ENTER> para continuar...")
      
      elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
            Módulo de Ingressos
                  """)
            print("_"*60)
            print("""
            Este módulo ainda está
            em desenvolvimento 
                  
                  """)
            print()
            input("Tecle <ENTER> para continuar...")
      
      elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
            Módulo de Relatórios
                  """)
            print("_"*60)
            print("""
            Este módulo ainda está
            em desenvolvimento 
                  
                  """)
            print()
            input("Tecle <ENTER> para continuar...")
      
      elif opcao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("_"*60)
            print(
                  """
            Sobre o Sistema
                  """)
            print("_"*60)
            print("""
            Projeto de Gestão de um Cinema
            
            Equipe de desenvolvimento:     
                  Eunice Cristina 
                  @cristinaeunice820@gmail.com
                    
                  
                  """)
      
            

agenda = []

start = True

while start:
    print("""
          ######################
          ###Programa agenda####
          ######################
          
          1 - Cadastrar contato
          2 - Pesquisar contato
          3 - Atualizar contato
          4 - Apagar contato
          5 - Listar todos 
          6 - Sair
          
          Escolha sua opção
          
          """)
    opcao = int(input(": "))
    if opcao  == 1:
        nome = input('\nDigite seu nome: ')
        tel = input('Digite seu telefone: ')
        end =input('Digite seu endereço: ')
        
        contato = [nome,tel,end]
        agenda.append(contato)
        
    elif opcao == 5:
        print('\nLista de contatos')
        for contato in agenda:
            
            print(f"""
                  Contato {agenda.index(contato)+1}
                  Nome :    {contato[0]}
                  Telefone: {contato[1]}
                  Endereço: {contato[2]}
                  """)
    elif opcao == 2:
        nome = input("\nDigite o nome que deseja pesquisar: ")
        exist=False
        for contato in agenda:
            if nome in contato:
                print(f"""\n
                  Contato {agenda.index(contato)+1}
                  Nome :    {contato[0]}
                  Telefone: {contato[1]}
                  Endereço: {contato[2]}
                  """)
                exist = True
        if not exist:
            print("\nContato não encontrado na agenda!")
    
    elif opcao == 3:
        print('\nEditar contato ->')
        nome = input("Digite o nome do contato que deseja editar: ")
        exist=False
        for contato in agenda:
            if nome in contato:
                nov_nome = input('\nDigite o nome do novo contato: ')
                tel = input('Digite o novo telefone: ')
                end = input('Digite o novo endereço: ')
                index = agenda.index(contato)
                agenda[index] = [nov_nome,tel,end]
                print('\nContato editado com sucesso!')
                exist = True
        if not exist:
            print("\nContato não encontrado na agenda!")
    
    elif opcao==4:
        nome = input("Digite o nome do contato que deseja deletar: ")
        exist=False
        for contato in agenda:
            if nome in contato:
                index = agenda.index(contato)
                del agenda[index]
                print('\nContato deletado com sucesso!')
                exist = True
        if not exist:
            print("\nContato não encontrado na agenda!")
        
            
        
        
    if opcao==6:
        break
    start = input('\nDeseja continuar? [S/N]: ').upper()
    if start=='N':
        start=False
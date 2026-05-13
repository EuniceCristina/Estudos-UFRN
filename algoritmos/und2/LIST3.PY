agenda = {}
add = True
print("Montando sua agenda--->")
while add:
    nome = input("Digite seu nome: ")
    tel = input("Digite seu telefone: ")
    data_nasc = input("Digite sua data de nascimento: ")
    agenda[nome]=[tel,data_nasc]
    stop = input('Deseja continuar? [s/n]: \n').upper()
    if stop=='N':
        add = False

consulta = input('Deseja consultar alguém da agenda? [S/N]: \n').upper()
add = True
while add:
    if consulta=='S':
        nome = input('Digite o nome a ser procurado: ')
        try:
            pessoa = agenda[nome]
            print(f"""
                Agenda
                
                Nome:                 {nome}
                Telefone:             {pessoa[0]}
                Data de nascimento:   {pessoa[1]}
                """)
        except:
            print(f'{nome} não encontrado n agenda!')
        stop = input('Deseja continuar proucurando? [s/n]: \n').upper()
        if stop=='N':
            add = False
else:
    print('Fim do programa.')
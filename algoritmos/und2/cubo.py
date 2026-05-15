banco = []
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
turnos = ['manhã','tarde','noite']
produtos=['Tapioca','Sanduba','Suco','Pastel','Coxinha']
for i in range(12):
    banco.append([])
    print(f'\nMês de {meses[i]} ')
    for t in range(3):
        banco[i].append([])
        print(f'Turno da {turnos[t]} - ')
        produtos_1 = []
        for p in range(0,len(produtos)):
            produto = int(input(f'Digite a quantidade de {produtos[p]}: '))
            banco[i][t].append(produto)
        

print()

for m in range(12):
    print(f'\nMês de {meses[m]} -')
    for t in range(3):
        print(f'\nTurno da {turnos[t]} :')
        for p in range(5):
            print(f'- {produtos[p]} : {banco[m][t][p]}')
        
        


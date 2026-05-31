from random import randint
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
            #produto = int(input(f'Digite a quantidade de {produtos[p]}: '))
            produto = randint(1,54)
            banco[i][t].append(produto)
        

print()

#for m in range(12):
 #   print(f'\nMês de {meses[m]} -')
 #   for t in range(3):
  #      print(f'\nTurno da {turnos[t]} :')
 #       for p in range(5):
   #         print(f'- {produtos[p]} : {banco[m][t][p]}')

print("\n\nVendas por mês: ")
for i in range(len(banco)):
    vendas_mes = 0
    for c in range(len(banco[i])):
        vendas_mes+=sum(banco[i][c])
    print(f'{meses[i]} : {vendas_mes}')

tarde,noite,manha = 0,0,0
for i in range(len(banco)):
    for c in range(len(banco[i])):
        if c==0:
            manha+=sum(banco[i][c])
        elif c==1:
            tarde+=sum(banco[i][c])
        else:
            noite+=sum(banco[i][c])

print("\n\nVendas por turno: ")
print(f'Manhã : {manha}')
print(f'Tarde : {tarde}')
print(f'Noite : {noite}')

tapioca,sanduba, suco, pastel, coxinha = 0,0,0,0,0

for i in range(len(banco)):
    for c in range(len(banco[i])):
        for p in range(len(banco[i][c])):
            if p == 0:
                tapioca+=banco[i][c][p]
            elif p == 1:
                sanduba+=banco[i][c][p]
            elif p == 2:
                suco+=banco[i][c][p]
            elif p == 3:
                pastel+=banco[i][c][p]
            elif p == 4:
                coxinha+=banco[i][c][p]

vendas_produto = [tapioca,sanduba,suco,pastel,coxinha]

print('\n\nVendas por produtos')
for i in range(len(produtos)):
    print(f'{produtos[i]} : {vendas_produto[i]}')
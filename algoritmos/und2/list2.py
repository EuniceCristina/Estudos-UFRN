temperaturas = []

for i in range(0,24,3):
    temp = float(input(f"Digite a temperaturas ás {i}hrs: "))
    temperaturas.append(temp)
media = sum(temperaturas)/8
print(f'Média diária de temperaturas: {media:.2f}°')
cont=0
print('Horários que a temperatura fcou acima da média:',end=" ")
for i in temperaturas:
    if i>media:
        print((temperaturas.index(i))*3,'hrs',end=' ')
        cont+=1
print("")
print(f'A temperatura esteve acima da média {cont} vezes.')
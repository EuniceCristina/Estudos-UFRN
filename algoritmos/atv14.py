#Escreva um programa em Python que leia a data_atual de nascimento de um
#usuário, obtenha a data_atual atual do sistema e calcule, exatamente, quantos
#anos ele possui, verificando se o usuário já completou ou não aniversário no ano atual.

import datetime

data_nasc = input("Digite a sua data de nascimento: ")
data_nasc = data_nasc.split("-")
data_atual = str(datetime.date.today())
data_atual = data_atual.split("-")

idade = int(data_atual[0])- int(data_nasc[2] )

if int(data_nasc[1])>int(data_atual[1]):  
    idade-=1
else:
    if int(data_nasc[0])>int(data_atual[2]):
        idade-=1
        
        

print(f"Seu idade é {idade}")
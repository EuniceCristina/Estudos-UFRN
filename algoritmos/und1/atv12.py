###Escreva um programa em Python que leia os nomes e as idades de dois usuários. O programa deve calcular e
#exibir na tela a diferença de idade entre eles. Independente da ordem em que os dados forem digitados, a diferença entre
#as idades deve ser exibida sempre como um valor positivo

user1 = input("Digite o nome do primeiro usuário: ")
idade1 = int(input("Digite a idade do primeiro usuário : "))
user2 = input("Digite o nome do segundo usuário : ")
idade2 = int(input("Digite a idade do segundo usuário : "))

if idade1>idade2:
    dif = idade1 - idade2
else :
    dif = idade2 - idade1
print(f"A diferença da idade de {user1} e {user2} é de {dif}!")
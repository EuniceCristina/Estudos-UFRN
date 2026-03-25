#Escreva um programa em Python que leia os nomes e as idades de dois usuários. 
# Em seguida, o programa deveverificar e exibir na tela quem é o mais velho e quem é o mais novo (exibir os 
# nomes dos usuários)

user1 = input("Digite o nome do primeiro usuário: ")
idade1 = int(input("Digite a idade do primeiro usuário : "))
user2 = input("Digite o nome do segundo usuário : ")
idade2 = int(input("Digite a idade do segundo usuário : "))

if idade1==idade2:
    print("Ambos tem a mesma idade!")
else:
    if idade1>idade2:
        print(f"{user1} é mais velho e {user2} é mais novo!")
    else:
        print(f"{user2} é mais velho e {user1} é mais novo!")
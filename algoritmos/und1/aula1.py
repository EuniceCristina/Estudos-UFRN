qrd_prt = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
numero = int(input("Digite um numero: "))
confirm = False

for i in qrd_prt:
    for x in qrd_prt:
        if i + x == numero:
            confirm = True
            
    

if confirm:
    print("Seu número é um quadrado perfeito resultado de uma soma de dois quadrados perfeitos")
else:
    print("Falso")
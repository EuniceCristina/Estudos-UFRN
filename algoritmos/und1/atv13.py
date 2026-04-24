#Escreva um programa em Python que determine se um determinado ano é ou
#não bissexto. Um ano é bissexto quando é divisível por 4 e não é divisível por 100,
#ou ainda, quando é divisível por 400.

print("Descobrindo se um ano é bissexto!")
ano = int(input("Digite o ano de análise: "))
if ano%4 == 0 and ano%100 != 0 or ano%400==0:
    print("Seu ano é bissexto")
else:
    print("Seu ano não é bissexto")

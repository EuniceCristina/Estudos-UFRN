import random
print("Advinhe o número...")
end = False
num = random.randint(1,9)
for cont in range(1,4):
    jog = int(input("Digite um número entre 1-9: "))
    
    if cont==1 or cont==2:
        if num==jog:
            if cont==1:
                print('Certa resposta. \nVOCÊ TEVE MUITA SORTE')
            elif cont==2:
                print("Certa resposta.\nVOCÊ JOGA BEM, MAS AINDA CONTOU SORTE")
                break
                  
        else:
            if num<jog:
                print("Você errou.Tente um número menor. ")
            else:
                print("Você errou.Tente um número maior. ")
    else:
        if num==jog:
            print("Certa resposta.VOCÊ É UM EXCELENTE ESTRATEGISTA")  
        else:
            print("ANALISE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE")

print("Fim do jogo.")
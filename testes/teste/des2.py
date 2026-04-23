import random
print("Advinhe o número...")
print("""
      PLACAR DE TENTATIVAS
      # tentativas  # pontos
      # 1           # 50
      # 2-4         # 25 
      # 5-7         # 15
      # 8-10        # 5
      """)
num = random.randint(1,100)
limite = [1,100]
tentativas = 0
for cont in range(1,11):
    jog = int(input("Digite um número entre 1-100: "))
    if jog<limite[0] or jog>limite[1]:
        print("Número inválido. Tente um número dentro do limite.")
    else:
    
        if num==jog:
            print('Certa resposta.Parabéns!')
            tentativas = cont
            break
                    
        else:
            if cont==11:
                    print("Você errou. Número de tentativas esgotadas!")
            else:
                if jog>num:
                    print("Você errou.Tente um número menor. ")
                    limite[1] = jog
                else:
                    print("Você errou.Tente um número maior. ")
                    limite[0] = jog

print("Fim do jogo.")
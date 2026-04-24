import random
import time
print("Advinhe o número...")
time.sleep(0.5)
print("""
      PLACAR DE TENTATIVAS
      # tentativas  # pontos
      # 1           # 50
      # 2-4         # 25 
      # 5-7         # 15
      # 8-10        # 5
      """)
pontos=0
time.sleep(1)
start = input('Deseja jogar? [S/N]: ').upper()
while start=='S':
    num = random.randint(1,100)
    limite = [0,101]
    tentativas=0
    for cont in range(1,11):
        jog = int(input("\nDigite um número entre 1-100: "))
        if jog<=limite[0] or jog>=limite[1]:
            print("\nNúmero inválido. Tente um número dentro do limite.")
        else:
            time.sleep(0.5)
            if num==jog:
                print('\nCerta resposta.Parabéns!')
                tentativas = cont
                break
                        
            else:
                if cont==10:
                        print("\nVocê errou. Número de tentativas esgotadas!")
                else:
                    if jog>num:
                        print("\nVocê errou.Tente um número menor. ")
                        limite[1] = jog
                    else:
                        print("\nVocê errou.Tente um número maior. ")
                        limite[0] = jog
    if tentativas>0:
        time.sleep(1)
        print(f"\nVocê acertou em {tentativas}° partida.")
        if tentativas==1:
            time.sleep(0.5)
            print('Total de pontos na partida: 50')
            pontos+=50
        elif tentativas>1 and tentativas<5:
            print('Total de pontos na partida: 25')
            time.sleep(0.5)
            pontos+=25
        elif tentativas>4 and tentativas<8:
            print('Total de pontos na partida: 15')
            time.sleep(0.5)
            pontos+=15
        else:
            print('Total de pontos na partida: 05')
            time.sleep(0.5)
            pontos+=5
        print(f"\nTotal de pontos: {pontos}")
        time.sleep(0.5)
    else:
        print("\nSem pontos acumulados")
        time.sleep(0.5)
        print(f"\nTotal de pontos: {pontos}")
        time.sleep(0.5)
    start = input("\nDeseja jogar novamente? [S/N]: ").upper()

time.sleep(0.5)
print(f"\nTotal de pontos: {pontos}")
time.sleep(0.5)
print("\nFim do jogo.")
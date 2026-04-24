from random import randint
import time
print('Zerinho ou um..')
time.sleep(1)
start = input("Deseja jogar? [S/N]: ").upper()
game = "S"
while start == 'S' and game=='S':
    jog = int(input("Digite sua jogada [0/1]: "))
    comp1 = randint(0,1)
    comp2 = randint(0,1)
    time.sleep(0.5)
    print(f"Computador 1 joga: {comp1}")
    time.sleep(0.5)
    print(f"Computador 2 joga: {comp2}")
    time.sleep(0.5)
    if jog==comp1 and jog==comp2:
        print("Empate!")
    elif jog!=comp1 and jog!=comp2:
        print('Parabens! Você ganhou.')
    elif comp1!=jog and comp2!=jog:
        print("Você perdeu! Computador 1 vence..")
    else:
        print("Você perdeu! Computador 2 vence..")
    time.sleep(1)
    game = input('Deseja continuar jogando? [S/N]: ').upper()
print("Fim de jogo!")
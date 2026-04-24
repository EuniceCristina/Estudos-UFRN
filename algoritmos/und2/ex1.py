from random import randint
import time
game = 'S'
print('Jogo dos dados..')
time.sleep(1)
start = input('Deseja jogar? [S/N]: ').upper()

while start=='S' and game =='S':
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    time.sleep(1)
    print(f'Dado 1: {dado1} | Dado 2: {dado2}')
    time.sleep(1)
    if dado1+dado2==7 or dado1+dado2==11:
        print('Parabens! Você ganhou.')
    else:
        print("Você perdeu! Computador vence..")
    time.sleep(2)
    game = input('Deseja continuar jogando? [S/N]: ').upper()
print('Fim de jogo!')
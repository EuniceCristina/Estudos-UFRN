import random
import time
game = 'S'
print('Pedra, papel, tesoura..')
time.sleep(1)
start = input('Deseja jogar? [S/N]: ').upper()

while start=='S' and game =='S':
    jog = input('Digite sua jogada [Pedra|Papel|Tesoura]\n: ').lower()
    opcoes = ['pedra','papel','tesoura']
    comp = random.choice(opcoes)
    time.sleep(1)
    print(f'Jogador: {jog} | Computador: {comp}')
    time.sleep(1)
    if jog==comp:
        print('Empate!')
    elif jog == 'papel' and comp=='pedra':
        print("Você ganhou! Papel ganha de pedra")
    elif jog == 'pedra' and comp=='papel':
        print("Você perdeu! Papel ganha de pedra")
    elif jog == 'pedra' and comp=='tesoura':
        print("Você ganhou! Pedra ganha de tesoura")
    elif jog == 'tesoura' and comp=='pedra':
        print("Você perdeu! Pedra ganha de tesoura")
    elif jog == 'tesoura' and comp=='papel':
        print("Você ganhou! Tesoura ganha de papel")
    elif jog == 'papel' and comp=='tesoura':
        print("Você perdeu! Tesoura ganha de papel")
    time.sleep(2)
    game = input('Deseja continuar jogando? [S/N]: ').upper()
print('Fim de jogo!')
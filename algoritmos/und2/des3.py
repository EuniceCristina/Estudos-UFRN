import random
import time
print("Desafie seu computador..")
print('Digite um número e veja se ele é capaz de adivinhar!')
start = input('Deseja jogar? [S/N]: ').upper()
while start=='S':
    jog = int(input("Digite seu núemero de 1-100: "))
    limite = [1,100]
    if not jog>=1 and jog<=100:
        print('Número inválido. Tente novamente.')
    else:
        for cont in range(1,8):
            comp = random.randint(limite[0],limite[1])
            time.sleep(2)
            print(f"\nAposta do computador : {comp}")
            if jog==comp:
                time.sleep(2)
                print('Computador vence!')
                break
            else:
                time.sleep(2)
                print("Computador falha.\n")
                time.sleep(1)
                print("\nNova tentativa: ")
                if comp>jog:
                    limite[1] = comp-1
                else:
                    limite[0] = comp+1
    start=input('\nDeseja jogar novamente? [S/N]: ').upper()
time.sleep(1)
print("Fim de jogo!")
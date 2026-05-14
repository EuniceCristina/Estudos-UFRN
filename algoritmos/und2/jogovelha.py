print('JOGO DA VELHA')

jogadas = 1
jogo = []
fim = False

for i in range(3):
    jogo.append([])
    for j in range(3) :
        jogo[i].append('-')


        
while jogadas <=9:
    
    possibilidades = [
        [jogo[0][0],jogo[0][1],jogo[0][2]],
        [jogo[1][0],jogo[1][1],jogo[1][2]],
        [jogo[2][0],jogo[2][1],jogo[2][2]],
        [jogo[0][0],jogo[1][0],jogo[2][0]],
        [jogo[0][1],jogo[1][1],jogo[2][1]],
        [jogo[0][2],jogo[1][2],jogo[2][2]],
        [jogo[0][0],jogo[1][1],jogo[2][2]],
        [jogo[0][2],jogo[1][1],jogo[2][0]]
    ]
    
    for linha in possibilidades:
        if linha[0]==linha[1]==linha[2] and linha[2]!='-':
            fim = True
            ganhador=linha[2]
        
    print("   0    1    2 ")
    for i in range(0,3):
        
        print(i,end=' ')
        for j in range(0,3):
            
            print(f' {jogo[i][j]}',end='   ')
        print('')
        
        
    if fim:
        print("FIM DE JOGO!")
        if ganhador == 'X':
            print("O jogador 1 venceu.")
        else:
            print("O jogador 2 venceu.")
        break
    
    
    
        
    if jogadas%2==1:
        print('Vez do jogador 1!')
        l = int(input('Digite a linha que deseja jogar:'))
        c = int(input("Deseja a coluna que deseja jogar:"))
        if jogo[l][c]=='-':
            jogo[l][c]='X'
        else:
            print("Posição indesponivél. Tente novamente")
            jogadas-=1
    else:
        print('Vez do jogador 2!')
        l = int(input('Digite a linha que deseja jogar:'))
        c = int(input("Deseja a coluna que deseja jogar:"))
        if jogo[l][c]=='-':
            jogo[l][c]='0'
        else:
            print("Posição indesponivél. Tente novamente")
            jogadas-=1
    
    
    
   
    
    jogadas+=1
print('JOGO DA VELHA')
from random import randint

jogadas = 1
jogo = []
fim = False

for i in range(3):
    jogo.append([])
    for j in range(3) :
        jogo[i].append('-')


        
while jogadas <=10:
    
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
    
        
    print("   0    1    2 ")
    for i in range(0,3):
        
        print(i,end=' ')
        for j in range(0,3):
            
            print(f' {jogo[i][j]}',end='   ')
        print('')
    
    if jogadas>9 and fim==False:
        print('\nEmpate!')
        break
    
    for linha in possibilidades:
        if linha[0]==linha[1]==linha[2] and linha[2]!='-':
            fim = True
            ganhador=linha[2]
        
        
    if fim:
        print("FIM DE JOGO!")
        if ganhador == 'X':
            print("Você venceu.")
        else:
            print("O computador venceu.")
        break
    
    
    
    
    
        
    if jogadas%2==1:
        print('Sua vez!')
        l = int(input('Digite a linha que deseja jogar:'))
        c = int(input("Deseja a coluna que deseja jogar:"))
        if jogo[l][c]=='-':
            jogo[l][c]='X'
            jogadas+=1
            
        else:
            print("Posição indesponivél. Tente novamente")
        
    else:
        
        
        
        print('Vez computador!')
        jogou = False
        
        for i in range (0,3):
            for j in range(0,3):
                if jogo[i][j]=='-':
                        
                        jogo[i][j] = '0'
                        
                        possibilidades = [
                        [jogo[0][0], jogo[0][1], jogo[0][2]],
                        [jogo[1][0], jogo[1][1], jogo[1][2]],
                        [jogo[2][0], jogo[2][1], jogo[2][2]],

                        [jogo[0][0], jogo[1][0], jogo[2][0]],
                        [jogo[0][1], jogo[1][1], jogo[2][1]],
                        [jogo[0][2], jogo[1][2], jogo[2][2]],

                        [jogo[0][0], jogo[1][1], jogo[2][2]],
                        [jogo[0][2], jogo[1][1], jogo[2][0]]
                    ]
                        venceu = False
                
                        for linha in possibilidades:
                            if linha[0]==linha[1]==linha[2] and linha[2]=='0':
                                venceu=True
                        if venceu:
                            jogou=True
                            jogadas+=1
                            break
                        else:
                            jogo[i][j]='-'
                
            if jogou:
                break
        
        if not jogou:
            for i in range (0,3):
                for j in range(0,3):
                    if jogo[i][j]=='-':
                        
                        jogo[i][j] = 'X'
                        possibilidades = [
                        [jogo[0][0], jogo[0][1], jogo[0][2]],
                        [jogo[1][0], jogo[1][1], jogo[1][2]],
                        [jogo[2][0], jogo[2][1], jogo[2][2]],

                        [jogo[0][0], jogo[1][0], jogo[2][0]],
                        [jogo[0][1], jogo[1][1], jogo[2][1]],
                        [jogo[0][2], jogo[1][2], jogo[2][2]],

                        [jogo[0][0], jogo[1][1], jogo[2][2]],
                        [jogo[0][2], jogo[1][1], jogo[2][0]]
                    ]
                    
                        venceu = False
                        for linha in possibilidades:
                            if linha[0]==linha[1]==linha[2] and linha[2]=='X':
                                venceu=True
                        if venceu:
                            jogo[i][j]='0'
                            jogou = True
                            jogadas += 1
                            break
                        else:
                            jogo[i][j]='-'
                if jogou:
                    
                    break
                
        if not jogou:
            if jogo[1][1]=='-':
                jogo[1][1]='0'
                jogou=True
                jogadas+=1
                
        
        if not jogou:
            cantos =[
                [0,0],
                [0,2],
                [2,0],
                [2,2]
                ] 

            for c in cantos:
                if jogo[c[0]][c[1]]=='-':
                    jogo[c[0]][c[1]]='0'
                    jogou=True
                    jogadas+=1
                    break

        if not jogou:
            for i in range (0,3):
                for j in range(0,3):
                    if jogo[i][j]=='-':
                        
                        jogo[i][j] = '0'
                        jogou=True
                        break
                if jogou:
                    jogadas+=1
                    break
    
    
    
    
                
                
            
            
    
    
    
    
    

    
    
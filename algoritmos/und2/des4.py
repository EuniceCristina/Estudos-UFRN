print("Qual seu time favorito?")
print("\nParticipe da nossa pesquisa!")

flamengo = 0
vasco = 0
corinthias = 0
fluminense = 0
palmeiras = 0
gremio = 0
santos = 0
nenhum = 0
total = int(input("Quantas pessoas participaram da pesquisa? "))

for i in range(0,total):
    print(f'\nPessoa {i+1}')
    voto = input('''Qual seu time?\nF - Flamengo, V - Vasco , C- Corinthias, E - Fluminense, P - Palmeiras, G - Grêmio , S - Santos ou N - Nenhum\n:''').upper()
    match voto:
        case "F":
            print("Você optou pelo Flamengo!")
            flamengo+=1
        case "V":
            print("Você optou pelo Vasco!")
            vasco+=1
        case "C":
            print("Você optou pelo Corinthias!")
            corinthias+=1
        case "E":
            print("Você optou pelo Fluminense!")
            fluminense+=1
        case "P":
            print("Você optou pelo Palmeiras!")
            palmeiras+=1
        case "G":
            print("Você optou pelo Grêmio!")
            gremio+=1
        case "S":
            print("Você optou pelo Santos!")
            santos+=1
        case "N":
            print("Você optou por nenhum!")
            nenhum+=1
        case _:
            print("Opção inválida. Tente novamente")
            total-=1
percFlamengo =  flamengo / total * 100
percVasco = vasco / total * 100
percCorinthias = corinthias/ total * 100
percFluminense = fluminense/ total * 100
percPalmeiras = palmeiras/ total * 100
percGremio = gremio/ total * 100
percSantos = santos/ total * 100
percNenhum = nenhum/ total * 100
listaPerc = {
    "1":[percCorinthias,corinthias,"Corinthias"],
    "2":[percFlamengo,flamengo,"Flamengo"],
    "3" :[percFluminense,fluminense,"Fluminense"],
    "4": [percGremio,gremio,"Grêmio"],
    "5": [percNenhum,nenhum,'Nenhum'],
    "6":[percPalmeiras,palmeiras,"Palmeiras"],
    "7":[percSantos,santos,'Santos'],
    "8":[percVasco,vasco,'Vasco']
}
ordenado = sorted(listaPerc.items(), reverse=True, key=lambda x: x[1])


    
print()
print("#"*40)
        
print("\nForam entrevistadas %d pessoas.\n"%total)

for time in ordenado:
    print(f"Escolheram o {time[1][2]}: %d pessoas\n"%time[1][1])
    print(f"Percentual de pessoas que preferem {time[1][2]}: {time[1][0]:.1f}% \n")

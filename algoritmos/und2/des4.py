print("Qual seu time favorito?")
print("\nParticipe da nossa pesquisa!")

flamengo = 0
vasco = 0
corinthias = 0
fluminense = 0
palmeiras = 0
gremio = 0
santos = 0
outro = 0
total = int(input("Quantas pessoas participaram da pesquisa? "))

for i in range(0,total):
    print(f'\nPessoa {i+1}')
    voto = input('''Qual seu time?\nF - Flamengo, V - Vasco , C- Corinthias, E - Fluminense, P - Palmeiras, G - Grêmio , S - Santos ou O - Outro\n:''').upper()
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
        case "O":
            print("Você optou por outro!")
            outro+=1
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
percOutro = outro/ total * 100
print()
print("#"*40)
print("\nForam entrevistadas %d pessoas.\n"%total)
print("Escolheram o Flamengo: %d pessoas\n"%flamengo)
print(f"Percentual de pessoas que preferem Flamengo: {percFlamengo:.1f}% \n")
print("Escolheram o Vasco: %d pessoas\n"%vasco)
print(f"Percentual de pessoas que preferem Vasco: {percVasco:.1f}% \n")
print("Escolheram o Corinthias: %d pessoas\n"%corinthias)
print(f"Percentual de pessoas que preferem Corinthias: {percCorinthias:.1f}% \n")
print("Escolheram o Fluminense: %d pessoas\n"%fluminense)
print(f"Percentual de pessoas que preferem Fluminense: {percFluminense:.1f}% \n")
print("Escolheram o Palmeiras: %d pessoas\n"%palmeiras)
print(f"Percentual de pessoas que preferem Palmeiras: {percPalmeiras:.1f}% \n")
print("Escolheram o Grêmio: %d pessoas\n"%gremio)
print(f"Percentual de pessoas que preferem Grêmio: {percGremio:.1f}% \n")
print("Escolheram o Santos: %d pessoas\n"%santos)
print(f"Percentual de pessoas que preferem Santos: {percSantos:.1f}% \n")
print("Escolheram por Outro: %d pessoas\n"%outro)
print(f"Percentual de pessoas que preferem outro time: {percOutro:.1f}% \n")
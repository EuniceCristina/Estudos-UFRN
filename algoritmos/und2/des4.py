print("Qual seu time favorito?")
print("\nParticipe da nossa pesquisa!")

flamengo = 0
vasco = 0
corinthias = 0
total = int(input("Quantas pessoas participaram da pesquisa? "))

for i in range(0,total):
    print(f'\nPessoa {i+1}')
    voto = input('''Qual seu time?\nF - Flamengo, V - Vasco ou C- Corinthias\n:''').upper()
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
        case _:
            print("Opção inválida. Tente novamente")
            total-=1
percFlamengo =  flamengo / total * 100
percVasco = vasco / total * 100
percCorinthias = corinthias/ total * 100
print()
print("#"*40)
print("\nForam entrevistadas %d pessoas.\n"%total)
print("Escolheram o Flamengo: %d pessoas\n"%flamengo)
print(f"Percentual de pessoas que preferem Flamengo: {percVasco:.1f}% \n")
print("Escolheram o Vasco: %d pessoas\n"%vasco)
print(f"Percentual de pessoas que preferem Vasco: {percFlamengo:.1f}% \n")
print("Escolheram o Corinthias: %d pessoas\n"%corinthias)
print(f"Percentual de pessoas que preferem Corinthias: {percCorinthias:.1f}% \n")
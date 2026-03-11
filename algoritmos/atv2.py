print("Calculando sua velocidade! (em pace)")
tempo = str(input("Qual seu tempo de corrida: "))
dist = float(input("Qual sua distância percorrida: (em km )"))
tempo = tempo.split(".")
for i in range(0,len(tempo)):
    tempo[i] = int(tempo[i])
t = sum(tempo)/60
vel = t/dist
print(f"Velocidade média do corredor em pace: {vel} " )
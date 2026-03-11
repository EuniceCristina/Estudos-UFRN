print("Calculando sua velocidade")
dist = float(input("Qual a sua distância ? (em km)"))
hora = str(input("Qual seu tempo ?"))
tmp = hora.split(".")
for i in range(0,len(tmp)):
    tmp[i] = int(tmp[i])
    
tempo = sum(tmp)/60
vel1 = dist/tempo
vel2 = vel1/3.6
print(f"Velocidade média do ciclista em km/h: {vel1} " )
print(f"Velocidade média do ciclista em m/s: {vel2} " )



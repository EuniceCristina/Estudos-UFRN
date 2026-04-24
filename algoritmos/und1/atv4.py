print("Calculando seu peso ideal!")
alt = float(input("Digite sua altura: "))
sexo = str(input("Digite seu sexo : [F/M]"))
alt = alt*100

if sexo.lower() == 'f':
    peso_ideal = (alt-100) - (alt-150)/2
else:
    peso_ideal = (alt-100) - ((alt-150)/4)
print(f"Seu peso ideal é : {peso_ideal:.2f}")

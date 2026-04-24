print("Calcule a area do seu ambiente")
com = float(input("Digite o comprimento do comodo(em m): "))
lar = float(input("Digite a largura do seu comodo(em m): "))
alt = float(input("Digite a altura do seu comodo(em m): "))
a1 = lar*com
a2 = lar*alt
a3 = com*alt
area_total = a1 + (2*a2) + (2*a3)
print(f"Sua area total é de {area_total} m²")
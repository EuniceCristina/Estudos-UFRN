print("Cálculo de IMC")
peso = float(input("Digite seu peso (em kg) : "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura)**2
print(f"Seu imc é de : {imc:.2f}")
print("""
TABELA DE VALORES DE IMC
PESO   RISCO
≤ 18,5 Abaixo do peso
18,6 - 24,9 Saudável
25,0 - 29,9 Sobrepeso
30,0 - 34,9 Obesidade Grau I (leve)
35,0 - 39,9 Obesidade Grau II (severa)
≥ 40,0 Obesidade Grau III (mórbida)
""")
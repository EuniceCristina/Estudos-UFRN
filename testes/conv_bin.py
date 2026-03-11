print("="*20,"TRADUTOR DE BINÀRIOS","="*20)
num = int(input("Digite seu número em decimal: "))
bin = []
while num >=1:
    resto = num % 2
    bin.insert(0, resto)
    num = num // 2

print (str(bin))


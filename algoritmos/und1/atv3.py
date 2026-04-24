print("Convertendo temperaturas ")
und = input("Deseja converter sua temperatura para celcius (C) ou Fahrenheit(F)? ")
if und=="F":
    tem_cel = float(input("Digite sua temperatura em celcius: "))
    tem_fah = 9/5 * tem_cel + 32
    print(f"Sua temperatura em fahrentheit é: {tem_fah}")
else:
    tem_fah = float(input("Digite sua temperatura em fahrenheit: "))
    tem_cel = 5/9 * (tem_fah - 32)
    print(f"Sua temperatura em celcius é: {tem_cel}")



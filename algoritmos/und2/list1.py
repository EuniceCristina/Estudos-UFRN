temperaturas = []

for i in range(0,6):
    temp = float(input(f'Digite a temperatura {i+1}: '))
    temperaturas.append(temp)
    
print(temperaturas)
temperaturas.reverse()
print(temperaturas)
temperaturas.sort()
print(temperaturas)
temperaturas.sort(reverse=True)
print(temperaturas)


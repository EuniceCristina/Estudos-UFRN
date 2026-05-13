import random
lista = []
soma = 0
for i in range(10):
  x = random.randint(1,100)
  lista.append(x)
  soma += x
print(soma/len(lista))
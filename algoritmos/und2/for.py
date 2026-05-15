#Q1 
print('Pares menores que 20, iniciando em zero:')
for i in range(20,-1,-2):
    print(i,end=' ')
print()

#Q2 Pares entre 40 e 20, incluindo-os
print("\nPares entre 40 e 20, incluindo-os:")
for i in range(40,19,-2):
    
    print(i,end=" ")
print()

# Q3. Ímpares entre 10 e 30
print("\nÍmpares entre 10 e 30")
for i in range(11,30,2):
    print(i,end=" ")

# Q4.
print("\nMúltiplos de 4 entre 1 e 25")
for i in range(4,25,4):
    print(i,end=" ")
print()

# Q5. 
print("\nDivisores de 30 entre 10 e 20")
for i in range(10,21):
    if 30%i==0:
        print(i,end=" ")
print()
# Q6. 
print("\nÍmpares menores que x ")
x = int(input("Digite seu valor:"))
for i in range(1,x,2):
    print(i,end=" ")
print()

# Q7. Múltiplos de 7 entre a e b (informado pelo usuário)
print("\nMúltiplos de 7 entre a e b ")
a = int(input("Valor de inicio(a): "))
b = int(input("Valor de finalização(b): "))

for i in range(a,b+1):
    if i%7==0:
        print(i,end=" ")
print()
numeros = []
for num in range(1, 6):
    numeros.append(int(input("digite um numero: ")))
maiorNumero = numeros[0]
cont = 1
while cont < len(numeros):
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    cont = cont + 1
print(' maior numero: '+ str(maiorNumero))
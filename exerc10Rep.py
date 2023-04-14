numero1=int(input("digite um numero "))
numero2=int(input("digite outro numero "))

while numero2<numero1:
	numero1=int(input("digite um numero "))
	numero2=int(input("digite outro numero "))
	
else:
	for i in range(numero1,numero2,1):
		print(i)
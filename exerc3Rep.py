nome=str(input("digite seu nome--> "))
while ( len(nome) <=  3 ):
	nome=str(input("Nome inválido. Digite novamente--> "))
	
idade=int(input("digite a idade"))
while ( idade > 150 or idade < 0 ):
	idade=int(input("digite sua idade"))
	
salario=float(input("digite seu salário"))
while ( salario < 0 ):
	salario=float(input("digite seu salário"))
	
sexo=str(input("digite a inicial do seu sexo"))
while  sexo !="F" and sexo!="M" :
	sexo=str(input("digite a inicial do seu sexo"))
	
estado_civil=str(input("digite a inicial do seu estado civil-->"))
while ( estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D" ):
	estado_civil=str(input("digite a inicial do seu estado civil-->"))
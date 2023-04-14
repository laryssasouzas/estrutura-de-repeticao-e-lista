país_a = int(input("população A = "))
taxaA =float(input("taxa de crescimento da população A = "))
result1 = taxaA * 0.01

país_b = int(input("população B = "))
taxaB =float(input("taxa de crescimento da população B = "))
result2 = taxaB * 0.01
ano = 0

while país_a <= país_b:
	país_a += país_a * result1
	país_b += país_b * result2
	ano += 1
print ( "país A ultrapassa ou iguala o país B em %d anos" %ano )
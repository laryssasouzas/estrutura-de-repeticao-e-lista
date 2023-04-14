
país_A = 80000
país_B = 200000
ano = 0

while país_A <= país_B:
	país_A += país_A * 0.03
	país_B += país_B * 0.015
	ano += 1

print ( "país A ultrapassa ou iguala a país B em %d anos" %ano )
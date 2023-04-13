idade = [16,18,25,30,53]
altura = [1.72, 1.64, 1.55, 1.85]
alturaVazia = []
idadeVazia = []
print(idade)
print(altura)

for i in range(5):
    idadeVazia.append(idade.pop())
    alturaVazia.append(altura.pop())

    print(idadeVazia)
    print(alturaVazia)
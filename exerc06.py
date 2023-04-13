aluno1 = [5,7,7,8]
aluno2 = [6,8,8,9]
aluno3 = [10,9,8,9]
aluno4 = [5,5,4,6]
aluno5 = [3,6,7,8]
aluno6 = [10,10,9,8]
aluno7 = [5,6,7,8]
aluno8 = [8,9,9,8]
aluno9 = [10,7,8,8]
aluno10 = [8,8,9,10]
alunos = [aluno1,aluno2,aluno3,aluno4,aluno5,aluno6,aluno7,aluno8,aluno9,aluno10]
contagem = 0
final = ""
media = 0

for i in alunos:
    for nota in alunos[contagem]:
        media = media + nota
        media = media / len(alunos[contagem])
        if media >= 7:
            final = f"{final} Aluno {contagem+1} (Aprovado) - {media} |"
            contagem +=1
            media = 0
            print("medias:", final)
exerc03 = [10,7.4,8.2,9.0]
media = 0
for i in range(0,len(exerc03)):
    print("nota", i+1, ":",exerc03[i])
    media = media + exerc03[i]
media = media / len(exerc03)
print("media:", media)

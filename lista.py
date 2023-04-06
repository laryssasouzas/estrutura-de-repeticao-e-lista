exerc01 = [1,2,3,4,5]
print(exerc01)

exerc02 = [10,9,8,7,6,5,4,3,2,1]
print(exerc02)

exerc03 = [10,7.4,8.2,9.0]
media = 0
for i in range(0,len(exerc03)):
    print("nota", i+1, ":",exerc03[i])
    media = media + exerc03[i]
media = media / len(exerc03)
print("media:", media)

exerc04 = ["a","b","c","d","e","f","g","h","i","j"]
for i in exerc04:
    if i not in "a,e,i,o,u":
        print(i)
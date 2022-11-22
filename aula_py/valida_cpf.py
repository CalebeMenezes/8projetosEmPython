cpf = '16899535009'
novo_cpf = cpf[:9]


reverso = 10
for index in range(19):
    if index > 8:
        index -= 9

    print(index, reverso)
    
    reverso -= 1 
    if reverso < 2:
        reverso = 11
 
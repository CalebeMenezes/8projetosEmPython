""" 
listas em python                                     
fatiamento
append > inserir no final da lista
insert > inserir no começo da lista ou qualquer um indice
pop > remover o ultimo elemento da lista
dei > deletar um elemento ou uma fatia de elementos da lista
clear > limpar a lista 
extend, + > juntar duas listas                
main, max
range > cria uma "lista" com a funçao "list"

booleanos = True or False
inteiros = 10
flutuante = -10.10
strings = 'textos'
"""

""" #lista = [1, 2, 3, 4, 'calebe', True, 10.5]  funçao lista suporta qualquer variavel de qualquer tamanho
#         0    1    2    3    4 
lista = ['A', 'B', 'C', 'D', 'E']   
#        -5   -4   -3   -2   -1

print(lista[0:3])   # lista suporta fatiamento == EX.[0:3] > começa no indice '0' e vai ate o '3' > o ultimo indice escolhido nao é mostrado
"""

""" 
#     0 1 2 3 4 5 6
l2 = [4,5,6,7,8,9,10]
l1.extend(l2)  # > l3 = l1 + l2
l2.append('b')
l2.insert(0, 'b')  # no "insert" devemos indicar em qual indice queremos colocar , EX. **.insert(5, "o que queremos colocar") > o 5 e a indicação que sera acrescentado no indice 5
l2.pop() # elimina o ultimo indice
del(l2[2:6]) # usa fatiamento para deletar os indices 
print(max(l2)) # mostra o maior valor da lista
print(min(l2)) # mostra o menor valor da lista


print(l2)

l1 = list(range(1,10)) # aqui ele esta criando uma lista de 1 a 9 o indice nao mostra, range us fatiamento EX. range(0, 100 ,8) > de 0 a 100 pulando de 8 em 8
print(l1)


l3 = [True, 'calebe', 10 , -10.5] 

for elem in l3:
    print(f'tipos de elem é {type(elem)} e seu valor é {elem}')  # aqui mostra os tipos dos indices e quais sao

"""

secreto = "deviluke"
digitadas = []
chances = 5

while True:
    if chances < 0:
        print('voce perdeu')
        break

    letra = input('digite uma letra: ')

    if len(letra) > 1:
        print('digite apenas uma letra')
        continue
    
    digitadas.append(letra)

    if letra in secreto:
        print(f'nice , essa letra "{letra}" faz parte da palavra')
    else:
        print(f'meee, essa letra "{letra}" nao faz parte da palavra')
        digitadas.pop()

    letra_secreta = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            letra_secreta += letra_secreta
        else:
            letra_secreta += '*'
    
    if letra_secreta == secreto:
        print(acertou)
        break    
    else:
        print(f'a palavra secreta esta assim "{letra_secreta}"')

    if letra_secreta not in secreto:
        chances -= 1
    print(f'voce ainda tem {chances} de chances')




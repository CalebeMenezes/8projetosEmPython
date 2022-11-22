'''
 39,40 
for / else  
if valor.startswith(''): > checagem de alguma letra na lista
if valor.lower().startswith(''): > nao importa se começa com letra maiuscula ou minuscula , faz a checagem completa

variavel = ['calebe', 'momo', 'lala']

ccm = False
for valor in variavel:
    if valor.lower().startswith('m'):
        ccm = True

if ccm:
    print('existe uma palavra com m')
else:
    print('nao exite uma palavra com m')

'''
'''
41
split, join and enumerate

split- divide uma string # STR
join- junta uma lista # STR
enumerate - enumera elementos da lista # list / objetos iteraveis

'''

string = "Que tal uma giradinha?, nunca olhe para uma tulipa."
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

for valor in lista_1: #iterando a lista
    print(valor)

for valor in lista_1:
    print( f'a palavra {valor} apareceu {lista_1.count(valor)}X vezes') # lista_1.count() - é usado para contar quantas palavra daquela que voce procura tem na lista






palavra = ''
contagem = 0
for valor in lista_1:
    qut_vezes = lista_1.count(valor)

    if qut_vezes > contagem:
        contagem = qut_vezes
        palavra = valor 
print(f'a palavra que apareceu mais vezes e {palavra.upper()} ({contagem}x)') 

for valor in lista_2:
    print(valor.strip().capitalize) # .strip tira os "espaços" do inicio e do fim  # .captalize deixa a primira letra maiuscula







string1 = ' lulu melhor sup'
lista_A = string1.split(' ')
string2 = ','.join(lista_A) # .join faz com que as listas se juntem

print(string2)






string3 = ' lulu melhor sup'
lista_B = string3.split(' ')

for v1, v2 in enumerate(lista_B):
    print(v1, v2, lista_B[v1])








'''
41
split, join, enumerate em python
* split - dividir uma string # str
* join - juntar uma lista # str
* enumerate - enumerar elementos da lista # iteraveis

'''

string = "lulu melhor sup"
lista = string.split('')

print(lista)

for valor in lista:
    print(f'a palavra {valor}apareceu{lista.count(valor)}vezes')



palavra = ''
contagem = 0
for valor in lista:
    qut_vezes = lista.count(valor)

    if qut_vezes > contagem:
        contagem = qut_vezes
        palavra = valor

print(f'a palavra que apareceu mais vezes e {palavra} ({contagem}x)')

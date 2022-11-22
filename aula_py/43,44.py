'''
43
desempacotamento de listas
'''

lista = ['calebe', 'evelyn', 'lulu','sei la']

n1, n2, *resto = lista

print(n1, n2)

'''
44
trocando valores entre variaveis
'''
x = 10 # Calebe
y = 'Calebe' # 19
x, y = y, x

print(f'x={x} e y={y}')

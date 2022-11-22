''' 
*32

manipulando stings
*strings indices 
*fatiamento de strings[inicio / fim / passo]
*função built-in len , abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.


# +     [012345678]      + == {positivo}
texto = 'Python s2'   #print( texto [2])  mostra o indice que escolher 
#print( len[texto]) fala quanto caracteres tem na string

#-     -[987654321]      - == {negativo}
#url = 'www.google.com.br/'
#print( url[:-1])  

nova_string = texto[2:6]
print(nova_string)


* 33

#while em python 
#utilizado para realizar açoes enquanto uma condição for verdadeira 
while True: #loop infinito  
    nome = input('Qual o seu nome? ')
    print(f'ola {nome}!')

# conta ate 10-1   ex:{123456789}
x = 0
while 0 < 10:
    print(x)
    x = x + 1


# pra pular algum numero  ex:{12 456789}
x = 0
while 0 < 10: 
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

#break quebra o laço (loop) 


x = 0
y = 0

while x < 10:
    
    while y < 5:
        print(f'o x vale {x} e y vale {y}')
        y += 1

    x += 1  # versão resumida do x = x + 1


# calculadora 

while True:
    print()
    num_1 = input('digite um numero')
    num_2 = input('digite outro numero')
    operador = input('digite um operador')

    if not num_1.isnumeric() or num_2.isnumeric():
        print('voce precisa digitar um numero')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / * 
    if operador == '+'
        print(num_1 + num_2)
    elif operador == '-'
        print(num_1 - num_2)
    elif operador == '/'
        print(num_1 / num_2)
    elif operador == '*'
        print(num_1 * num_2)
    else:
        print('operador invalido')


*34

#acumuladores 
#contadores
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1

'''    
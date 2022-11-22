'''
#!
print("olá mundo!")
print("hoje é")
print("27","03","2020", sep = "/")

x = 100
y = 200

if x > y:
	print("x é maior do y")
else:
	print("x não é maior do que y")	
	if y > x:
		print("y é maior do que x")
	else:
		print("y não é maior do que x")	
'''
#//////////////////////////////////////////////////////////////
'''
#2
#str - string = tudo que estiver entre as aspas

print("essa é uma 'string' (str).")

print("esse é meu \"texto\". ")

print("esse é meu \n (str).") # \n = quebra de linha 

print(r"esse é meu \n (str).") # (r)= o que estiver dentro das aspas vai ser mostrado sem ser executado
'''
#//////////////////////////////////////////////////////////////
'''
#3
"""
tipos de dados: 
str = string - textos entre aspas ""/''
int = inteiro- 123456 ; 0 -10 -20 -50
float = real/ponto flutuante - 10.50; 1,5 ; -10.10
bool = booleano/logico - true/false; 10==10 
""" 
print("calebe", type("Calebe")) # str

print(10, type(10)) # int

print(-10.10, type(-10.10)) # float

print(10==10, type(10==10)) # bool
print("c"=="c", type("c"=="c")) # bool 
print("c"=="C", type("c"=="C")) # bool

print("calebe",type("calebe"), bool("calebe")) # converte em ou7tro valor
print("10",type("10"), type(int("10"))) 
print("calebe", float("10.5"))
print(10 + 10)

#exercicio 
 
print("calebe", type("calebe"))
print(18, type(18))
print(1.70, type(1.70))
print(18 > 18 , type(18 > 18))
'''
#//////////////////////////////////////////////////////////////
'''
#4
"""
operadores aritimeticos:
+ , - , * , / , // , ** , % , ()
soma, subtração, multiplicar, divisao
divisao inteira, exponenciação, modulo
alterar a precedência
"""

print(10 * 10) # multiplicação 
print(10 * "a") # repetição 
print(10 + 10) # soma
print('5' + '5') # concatenação / ligação
print("calebe" + " " + "menezes e ele tem" + str(18) + "anos")
print(10 - 10) # subtrtação
print(10 / 10) # divisão
print(10.5 // 3) # divisão inteira
print(2 ** 10) # exponenciação
print(10 % 3) # modulo / resto 
print(5+2*10)
print((5=2)*10) # vai fazer primiro o que esta em parenteses
'''
#//////////////////////////////////////////////////////////////
'''
#5

# vairaveis = iniciar com letra , pode conter numeros ,separa _, letras minusculas


nome = "calebe" # valor de atribuição
idade = 18
altura = 1.80
é_maior = idade == 18 # nome composto separa com _;
data_atual = 2020
peso = 70
imc = 21.60 # peso / (altura ** 2)
# variaveis nao podem começar com numeros

print('nome', nome, sep='--')
print('idade', idade, sep='--')
print('altura', altura, sep='--')
print('é_maior', é_maior, sep='--')

print(idade * altura)
print(data_atual / (idade * altura))
print(nome, 'tem', idade, 'de idade e seu imc', imc)
'''
#//////////////////////////////////////////////////////////////
'''
#6
nome = 'calebe'
idade = 18 
altura =1.80
peso = 70
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} de idade e seu imc é {imc:.2f}')
# o 'F' antes de tudo significa = fstring = serve para formatar o print
# os :.2 serve para escolher ate quantas casas mostrar 
print('{} tem {} de idade e seu imc é {} '. format(nome, idade, imc))
print('{0} tem {1} de idade e seu imc é {2} '. format(nome, idade, imc))
#posso colocar letra ou numeros para simbolisar os dados entre {}.
'''
#//////////////////////////////////////////////////////////////
'''
#7

# entrada de dados 


#input("qual o seu nome?") # input serve para pegar os dados do usuarios
nome = input("qual o seu nome?") # o que o usuario escrever vai ser a variavel
print(f"o usuario digitou {nome} e o tipo da variavel é" f"{type(nome)}")
# qualquer coisa que o usuario digitar no codigo 'input' vai ser 'str'
idade = input("qual a sua idade? ")

print(f'{nome} tem {idade} anos')

#ano_nascimento = 2020 - idade # se deixar assim vai dar erro , temos que formatar o tipo
ano_nascimento = 2020 - int(idade)

numero_1 = int(input('digite um numero: '))
numero_2 = int(input('digite outro numero : '))

print(numero_1 + numero_2)
print(numero_1 **  numero_2)
'''
#//////////////////////////////////////////////////////////////
'''
#8

# condições IF, ELIF e ELSE 


if False:
	print("verdadeira")
elif True:
	print("agora é verdadeiro")
else:
	print("não é verdadeira")
'''
#//////////////////////////////////////////////////////////////
'''
#9

# operadores relacionais 
# ==  igualdede
# > maior que
# >= maior que ou igual a
# < menor que 
# <= menor que ou igual a 
# != diferente


nome = input('qual o seu nome?')
idade = input('qual sua idade?')
idade_menor = 20 
idade_maior = 20


idade = int(idade)

if idade >= idade_menor and idade <= idade_maior:
	print(f'{nome} pode pegar emprestimo.')
else:
	print(f'{nome} não pode pegar emprestimo.')
'''
#//////////////////////////////////////////////////////////////
'''
#10
usuario = input("digite seu usuario")
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))
if qtd_caracteres < 6:
	print('você precisa pelo menos 6 caracteres')

else:
	print('você foi cadastrado no sistema')

'''
'''

string1 = input('digite alguma coisa')
string2 = input('digite outra coisa')

print(f'a quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
# len conta a quantidade de caracteres em uma string , não funciona com numeros
'''
#//////////////////////////////////////////////////////////////
'''
#11
num1 = input("digite um numero: ")
num2 = input("digite outro numero: ")

# isnumeric / isdigit / isdecimal
#numeros e positivos (123454321)

''
if num1.isdigit() and num2.isdigit()
	num1 = int(num1)
	num2 = int(num2)

	print(num1 + num2)
else:
	print("nao pude converter os numeros para realizar contasa")	
''

try:
	num1 = float(num1)
	num2 = float(num2)

	print(num1 + num2)
except:
	print('error')
'''
#//////////////////////////////////////////////////////////////
'''
#12
valor = false 


if valor:
	pass  # codigo "pass" pode ser usado para passar o codigo para depois eu escrever
else:
    print("tchau")
'''
#//////////////////////////////////////////////////////////////
'''
#15
''
formatando valores com modificadores 

:s - texto (string)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:. (numero)f - quantidade de casas decimais (float)
;(caractere)(> ou < ou ^)(quantidade)(tipo- s, d ou f)
> - esquerda
< - direita
^ - centro
''
num1 = 10
num2 = 3
divisao = num1 / num2
print("{:.2f}".format(divisao))

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0^10}')

print(f'{num_2:.2f}')

print(f'{num_2:0>10.2f}')

nome = "calebe"
print( 50-len(nome) / 2)
#print(f'{nome:#^50}')
#sobrenome = "menezes"
#ome_formatado = '{1}'.format(nome, sobrenome)
#pritn(nome_formatado)


print(nome.lower())# tudo minusculo
print(nome.upper())# tudo maiusculo 
print(nome.title())# primeira letra maiuscula
'''
#//////////////////////////////////////////////////////////////
'''
#13
"""
 mainupulando strings--
 *string indices
 *fatiamento de string (inicio / fim / passo)
 *funloes nuit-in len, abs, type, print, etc...
 essas funçoes podem ser usadas diretamente em cada tipo.
"""
# positivos [0,1,2,3,4,5,6,7,8]
texto = 'python s2'
#negativo [9,8,7,6,5,4,3,2,1]

url = "www.google.com/"
print(url[:-1])

print(texto[8])
nova_string = texto[:6]
print(nova_string)
'''
#//////////////////////////////////////////////////////////////
'''
#teste 
nome = 'calebe'
idade = 20
altura = 1.80
peso = 70.5
ano_atual = 2021
ano_que_nasci = ano_atual - idade
imc = peso / (altura ** 2)

print(ano_atual - idade)
print('imc é igual a', peso / (altura ** 2))
print(f'{nome} tem {idade} de idade {altura} de altura {peso} de peso seu imc é {imc:.2f} e o ano em que nasceu foi {ano_que_nasci}')
print('{} tem {} de idade sau altura é {} seu peso é {} seu imc é {} e o ano em que nasceu foi {}'. format(nome, idade, altura, peso, imc, ano_que_nasci))

print("my name is {}".format(nome))
print(f"my name is {nome})
'''
#//////////////////////////////////////////////////////////////
'''
#exercicio
usuario = input("digite um numero inteiro: ")
if usuario.isdigit():
	usuario = int(usuario)
	if usuario % 2 == 0:
		print(f"{usuario} par")
	else:
		print(f"{usuario} impar")			
else:
	print("isso nao pe um numero inteiro")	
qtd_num = len(usuario)
print(usuario, qtd_num, type(qtd_num))
if qtd_num =(2,4,6,8,10):
	print("o numero é par")
else qtd_num =(1,3,5,7,,9):
	print("o numero é impar")

adm = input("digite a hora: ")
adm = int(usuario)
hora = len(usuario)

if hora = (0,1,2,3,4,5,6,7,8,9,10,11):
	print("bom dia")
else hora = (12,13,14,15,16,17):	
	print("boa terde")
else hora = (18,19,20,21,22,23):
	print("boa noite")


pessoa = input("digite seu nome: ")	
qtd_caract = len(pessoa)

print(pessoa, qtd_caract, type(qtd_caract))

if qtd_caract <= 4:
	print("seu nome é curto")
else qtd_caract >=7:
	print("seu nome é grande")
else qtd_caract = 5,6:
	print("seu nome é normal")
'''
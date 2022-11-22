""" 35
#indices 
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_usuario = input('Quais letras voce deseja mudar para maiuscula?') # aqui o usuario pode digitar a letra que ele quer mudar para maiuscula """

""" while contador < 10:
    print(frase[contador],contador)
    contador += 1
 """

""" while contador < tamanho_frase:  #aqui mostra a frase e o numero respectivo de cada
    print(frase[contador],contador)
    contador += 1 """

""" while contador < tamanho_frase: #aqui ele concatena a frase em uma nova string   
    nova_string += frase[contador]
    contador += 1
    print(nova_string)
 """

""" while contador < tamanho_frase:  # aqui ele muda alguma letra que o usuario escolher , podendo ficar maiusculo ou minusculo
    letra = frase[contador]
    if letra == input_usuario
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1  """

""" 36
for in em python
iterando strings com for
funçao range(start=0, stop, step=1) # função 'range' não depende da função 'for' e vice versa 

texto = 'Python' """

""" for letra in texto:  # jeito mais simples de mostra as letra e a palavra na string
    print(letra)
 """

""" for n, letra in enumerate(texto):  # jeito mais simples de mostra as letra e a palavra na string e mostrar a numeração
    print(n,letra) """

""" for n in range(10): # range por padrão vem assim > range(0, ** ,1) >> **== qualquer numero 
    print(n)        # normalmete o range conta somando , mas se colocar range(20 , 10 , -1) ele ira para traz  
                    # range(0 , ** , 1) 0= o começo 'onde voce ira colocar algum numero', ** = onde ele ira parar , 1= de quanto em quanto irar pular
 """

""" for n in range(100):
    if n % 8 == 0:     # % =  mostra o resto da divisão 
        print(n)

 """




'''
45
operaçoes ternarias
''' 

from _typeshed import IdentityFunction


logged_user = True
msg = 'usuario logado' if logged_user else 'usuario precisa logar'

print(msg)

idade = input('qual sua idade?')

if not idade.isnumeric():
    print('voce precisa digitar apenas numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg =  'pode entrar' if e_de_maior else 'nao pode entrar'

    print(msg)
'''
if logger_user:
    msg = 'usario logado'
else:
    msg = 'usuario precisa logar'
print(msg)"
'''


'''
46
expressoes condicionais com operador OR
'''

nome = input('qual seu nome?')

print(nome or 'voce nao digitou nada')

